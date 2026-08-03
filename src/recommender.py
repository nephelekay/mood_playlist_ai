from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    track_id: str
    title: str
    artists: str
    album: str
    genre: str
    mood: str
    energy: float
    tempo: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genres: list[str]
    favorite_artists: list[str]
    favorite_moods: list[str]

    target_energy: float
    target_tempo: float
    target_valence: float
    target_danceability: float
    target_acousticness: float
    


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        """
        Initializes the recommender with a list of songs.

        Args:
            songs: A list of Song objects.
        """
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """
        Recommends the top k songs that best match the user's preferences.

        Args:
            user: The user's music preferences.
            k: Number of recommendations to return.

        Returns:
            A list of the top k Song objects.
        """
        # Convert the UserProfile into a dictionary so score_song() can be reused.
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }

        scored_songs = []

        # Score every song in the catalog.
        for song in self.songs:
            song_dict = {
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
                "acousticness": song.acousticness,
            }

            score, _ = score_song(user_prefs, song_dict)
            scored_songs.append((song, score))

        # Sort songs by score from highest to lowest.
        scored_songs.sort(key=lambda item: item[1], reverse=True)

        # Return only the top k songs.
        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """
        Generates an explanation for why a song was recommended.

        Args:
            user: The user's music preferences.
            song: The song being explained.

        Returns:
            A string describing why the song matches the user's preferences.
        """
        # Convert the UserProfile into a dictionary.
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }

        # Convert the Song object into a dictionary.
        song_dict = {
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "acousticness": song.acousticness,
        }

        # Reuse the scoring function to generate the explanation.
        _, reasons = score_song(user_prefs, song_dict)

        return ", ".join(reasons)

    """
    Reads songs from a CSV file and returns them as a list of dictionaries.
    Numeric values are converted to floats so they can be used in scoring 
    calculations.
    @param csv_path CSV to parse.
    @return list of song dictionaries.
    """
    def load_songs(csv_path: str) -> List[Dict]:

        print(f"Loading songs from {csv_path}...")

        songs = []

        with open(csv_path, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            # Read each row and store only the fields used by the recommender.
            for row in reader:
                # Each dictionary represents one song
                song = {
                    "track_id": row["track_id"],
                    "title": row["track_name"],
                    "artist": row["artists"],
                    "album": row["album_name"],
                    "genre": row["track_genre"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }

                songs.append(song)

            return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Calculates a recommendation score for a single song.

    Songs earn points for matching the user's preferred genre and mood,
    having a similar energy level, and matching the user's acoustic
    preference.

    Args:
        user_prefs: Dictionary containing the user's preferences.
        song: Dictionary containing one song's information.

    Returns:
        A tuple containing:
        - The total score.
        - A list of reasons explaining how the score was calculated.
    """
    score = 0.0
    reasons = []

    # Award points for a matching genre.
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 30
        reasons.append("Genre match (+30)")

    # Award points for a matching mood.
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 20
        reasons.append("Mood match (+20)")

    # Reward songs with energy levels close to the user's target.
    energy_difference = abs(song["energy"] - user_prefs["target_energy"])
    energy_score = max(0, 15 - (energy_difference * 15))
    score += energy_score
    reasons.append(f"Energy similarity (+{energy_score:.1f})")

    # Award points based on the user's acoustic preference.
    if user_prefs["likes_acoustic"]:
        if song["acousticness"] >= 0.70:
            score += 5
            reasons.append("High acousticness (+5)")
    else:
        if song["acousticness"] < 0.70:
            score += 5
            reasons.append("Low acousticness (+5)")

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
) -> List[Tuple[Dict, float, str]]:
    """
    Scores every song, ranks them, and returns the top recommendations.

    Args:
        user_prefs: Dictionary containing the user's preferences.
        songs: List of song dictionaries.
        k: Number of recommendations to return.

    Returns:
        A list of tuples containing:
        (song dictionary, score, explanation).
    """
    recommendations = []

    # Score every song in the catalog.
    for song in songs:
        score, reasons = score_song(user_prefs, song)

        # Convert the list of reasons into a readable sentence.
        explanation = ", ".join(reasons)

        recommendations.append((song, score, explanation))

    # Sort recommendations by score from highest to lowest.
    recommendations.sort(key=lambda recommendation: recommendation[1], reverse=True)

    # Return only the top k recommendations.
    return recommendations[:k]