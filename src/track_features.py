from typing import List
from dataclasses import dataclass
import csv

#Excluded genres from data for more targeted track similarity
EXCLUDED_GENRES = {
    "chill",
    "club",
    "groove",
    "party",
    "romance",
    "sad",
    "guitar",
    "piano",
    "british",
    "french",
    "german",
    "indian",
    "iranian",
    "malay",
    "spanish",
    "swedish",
    "turkish",
    "brazil"
}

@dataclass
class Song:
    """
    Represents song and features.
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
    Represents user's taste preferences.
    """
    favorite_genres: list[str]
    favorite_artists: list[str]
    favorite_moods: list[str]

    target_energy: float
    target_tempo: float
    target_valence: float
    target_danceability: float
    target_acousticness: float


def createUserProfile(songs: List[Song]) -> UserProfile | None:
    """Creates user profile based on preferences.

    The user's favorite songs are matched against available songs, and
    their average features are used to create target preferences.

    Args:
        songs: List of Song objects to match against user's input.

    Returns:
        UserProfile containing user's preferences, or none the
        entered songs are not found.
    """
    user_songs = input("Give me 3 or more favorite songs (separated by commas):")
    print("Genre + Artists are optional (to skip hit enter)")
    user_genres = input("     What genres do you like? (separate by commas): ")
    user_artists = input("    Who are your favorite artists? (separate by commas): ")

    top_songs = [
        cleanText(user_song)
        for user_song in user_songs.split(",")
        if user_song.strip()
    ]

    top_genres = [
        cleanText(user_genre)
        for user_genre in user_genres.split(",")
        if user_genre.strip()
    ]

    top_artists = [
        cleanText(user_artist)
        for user_artist in user_artists.split(",")
        if user_artist.strip()
    ]

    matching_songs = [] #Find songs from dataset that match user's favorites
    for song in songs:
        if cleanText(song.title) in top_songs:
            matching_songs.append(song)

    if len(matching_songs) == 0: return None
    song_count = len(matching_songs)

    user = UserProfile( #Build profile using average features of matched songs
        favorite_genres=top_genres,
        favorite_artists=top_artists,
        favorite_moods=[song.mood for song in matching_songs],

        target_energy=sum(song.energy for song in matching_songs) / song_count,
        target_tempo=sum(song.tempo for song in matching_songs) / song_count,
        target_valence=sum(song.valence for song in matching_songs) / song_count,
        target_danceability=sum(song.danceability for song in matching_songs) / song_count,
        target_acousticness=sum(song.acousticness for song in matching_songs) / song_count
    )

    return user


def cleanText(text: str) -> str:
    """Normalizes text to compare against dataset strings.

    Args:
        text: Text to normalize.

    Returns:
        Lowercase text with leading and trailing whitespace removed.
    """
    return text.lower().strip()


def generateMood(energy: float, valence: float, acousticness: float) -> str:
    """Assigns mood based on a song's features.

    The mood is determined using energy, valence, and acousticness ranges
    to categorize songs into mood groups.

    Args:
        energy: Measure of song's intensity.
        valence: Measure of song's positive or negative emotional tone.
        acousticness: Measure of song's acoustic characteristics.

    Returns:
        Mood assigned to song.
    """
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



def loadSongs(csv_path: str) -> List[Song]:
    """Loads songs from CSV file and converts them into Song objects.

    Features with numeric values are converted to floats, excluded genres are
    filtered out, and a mood generated.

    Args:
        csv_path: Path to the CSV file containing song data.

    Returns:
        List of Song objects created from CSV data.
    """
    print(f"Loading songs from {csv_path}...")

    songs = []

    with open(csv_path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:

            if row["track_genre"].lower() in EXCLUDED_GENRES:
                continue

            mood = generateMood(
                float(row["energy"]),
                float(row["valence"]),
                float(row["acousticness"])
            )

            songs.append(
                Song(
                    track_id=row["track_id"],
                    title=row["track_name"],
                    artists=row["artists"],
                    album=row["album_name"],
                    genre=row["track_genre"],
                    mood=mood,
                    energy=float(row["energy"]),
                    tempo=float(row["tempo"]),
                    valence=float(row["valence"]),
                    danceability=float(row["danceability"]),
                    acousticness=float(row["acousticness"]),
                )
            )

    return songs


 