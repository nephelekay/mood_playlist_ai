import random
from src.track_features import Song, UserProfile
from src.scoring import scoreSong

MOOD_GENRES = { # Mapping playlist moods to subgenres
    "acoustic": {
        "acoustic",
        "folk",
        "singer-songwriter",
        "indie",
        "guitar"
    },

    "party": {
        "dance",
        "pop",
        "edm",
        "hip-hop",
        "club",
        "disco",
        "house"
    },

    "dark": {
        "metal",
        "heavy-metal",
        "black-metal",
        "death-metal",
        "goth",
        "industrial",
        "hard-rock"
    },

    "energetic": {
        "rock",
        "metal",
        "punk",
        "dance",
        "edm",
        "hardstyle",
        "drum-and-bass"
    },

    "feel-good": {
        "pop",
        "disco",
        "funk",
        "soul",
        "dance",
        "indie-pop"
    },

    "laid-back": {
        "chill",
        "ambient",
        "jazz",
        "folk",
        "acoustic",
        "soul"
    },

    "melancholic": {
        "indie",
        "alternative",
        "emo",
        "singer-songwriter",
        "folk",
        "ambient"
    },

    "chill": {
        "chill",
        "ambient",
        "acoustic",
        "jazz",
        "indie",
        "trip-hop"
    }
}

def recommendSongs( songs: list[Song], user: UserProfile, number_of_songs: int = 25) -> list[tuple[Song, float, list[str]]]:
    """Generates ranked list of song recommendations based on user profile.

    Args:
        songs: List of available Song objects to shift through.
        user: UserProfile object containing profile features.
        number_of_songs: Maximum number of recommendations to return.

    Returns:
        Sorted list of tuples containing (Song, score, list_of_reasons).
    """
    recommendations = []

    seen = set()

    for song in songs:
        if song.title in seen: continue
        score_info = scoreSong(song, user)

        score = score_info[0] ##Actual score
        reasons = score_info[1] ##Reasoning for scoring

        recommendations.append((song, score, reasons))
        seen.add(song.title)

    recommendations.sort( 
        key=lambda recommendation: recommendation[1], ##Sort recommended songs
        reverse=True
    )

    return recommendations[:number_of_songs] ##List of 25 songs(track, score, reasons)

def generateMoodPlaylist(songs: list[Song], mood: str, number_of_songs: int = 25):
    """Generates playlist based on selected mood.

    Songs scored based on whether their calculated mood matches the one
    selected and whether their genre fits the mood's associated genres. 
    The songs that are strong matches are then randomly selected to create a 
    different playlist each time.

    Args:
        songs: List of available Song objects to choose from.
        mood: Mood to use when generating the playlist.
        number_of_songs: Maximum number of songs to include in the playlist.

    Returns:
        List of tuples containing (Song, score, list_of_reasons).
    """

    playlist = []

    selected_mood = mood.strip().lower()

    for song in songs:
        score = 0
        reasons = []

        # Song matches mood
        if song.mood.lower() == selected_mood:
            score += 1.0
            reasons.append("Matched playlist mood")

        # Song genre matches mood's associated genres
        if song.genre.lower() in MOOD_GENRES[selected_mood]:
            score += 0.5
            reasons.append("Fits the style of this playlist")

        if score > 0:
            playlist.append((song, score, reasons))

    # Sort song based on score
    playlist.sort(
        key=lambda recommendation: recommendation[1],
        reverse=True
    )

    # Remove duplicate titles (only handles absolute copies of a song)
    seen_titles = set()
    unique_playlist = []

    for recommendation in playlist:
        song = recommendation[0]
        title = song.title.strip().lower()

        if title not in seen_titles:
            unique_playlist.append(recommendation)
            seen_titles.add(title)
    ##Randomly select top candidate songs(playlist during run is unique)
    candidate_pool = unique_playlist[:75] 
    return random.sample(
        candidate_pool,
        min(number_of_songs, len(candidate_pool))
    )