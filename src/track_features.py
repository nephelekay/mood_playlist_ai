from typing import List
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
    

def generate_mood(energy: float, valence: float, acousticness: float) -> str:
    # Strong acoustic sound
    if acousticness > 0.75 and energy < 0.60:
        return "Acoustic"

    # High-energy celebrations
    if energy > 0.85 and valence > 0.70:
        return "Party"

    # High-energy but darker tone
    if energy > 0.80 and valence < 0.30:
        return "Dark"

    # High-energy general
    if energy > 0.75:
        return "Energetic"

    # Positive and upbeat
    if valence > 0.70:
        return "Feel-Good"

    # Relaxed and positive
    if energy < 0.40 and valence > 0.50:
        return "Laid-Back"

    # More emotional or introspective
    if energy < 0.55 and valence < 0.35 and acousticness > 0.40:
        return "Melancholic"

    # Relaxed regardless of emotion
    if energy < 0.45:
        return "Chill"


    return "Neutral"   


"""
Reads songs from a CSV file and returns them as Song objects.
Numeric values are converted to floats and moods are generated
from audio features.
@param csv_path CSV file to parse.
@return list of Song objects.
"""
def load_songs(csv_path: str) -> List[Song]:

    print(f"Loading songs from {csv_path}...")

    songs = []

    with open(csv_path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        # Read each row and store only the fields used by the recommender.
        for row in reader:
            mood = generate_mood(float(row["energy"]), float(row["valence"]), float(row["acousticness"]))
            songs.append(
                Song(
                    track_id = row["track_id"],
                    title = row["track_name"],
                    artists = row["artists"],
                    album = row["album_name"],
                    genre = row["track_genre"],
                    mood=mood,
                    energy = float(row["energy"]),
                    tempo = float(row["tempo"]),
                    valence = float(row["valence"]),
                    danceability = float(row["danceability"]),
                    acousticness = float(row["acousticness"]),
                )
            )
            
        return songs
    



 