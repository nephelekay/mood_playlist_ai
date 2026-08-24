import random
from src.track_features import Song, UserProfile
from src.scoring import scoreSong

MOOD_GENRES = {
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
    recommendations = []

    seen = set()

    for song in songs:
        if song.title in seen: continue
        score_info = scoreSong(song, user)

        score = score_info[0] ##Returns actual score
        reasons = score_info[1] ##Returns reasoning for scoring

        recommendations.append((song, score, reasons))
        seen.add(song.title)

    recommendations.sort(
        key=lambda recommendation: recommendation[1],
        reverse=True
    )

    return recommendations[:number_of_songs] ##Rerurns list of 25 songs(track, score, reasons)

def generateMoodPlaylist(
    songs: list[Song],
    mood: str,
    number_of_songs: int = 25
):
    playlist = []

    selected_mood = mood.strip().lower()

    for song in songs:
        score = 0
        reasons = []

        # Primary match: song's assigned mood
        if song.mood.lower() == selected_mood:
            score += 1.0
            reasons.append("Matched playlist mood")

        # Secondary match: genre associated with the mood
        if song.genre.lower() in MOOD_GENRES[selected_mood]:
            score += 0.5
            reasons.append("Fits the style of this playlist")

        if score > 0:
            playlist.append((song, score, reasons))

    # Highest-scoring songs first
    playlist.sort(
        key=lambda recommendation: recommendation[1],
        reverse=True
    )

    # Remove duplicate song titles
    seen_titles = set()
    unique_playlist = []

    for recommendation in playlist:
        song = recommendation[0]
        title = song.title.strip().lower()

        if title not in seen_titles:
            unique_playlist.append(recommendation)
            seen_titles.add(title)

    # Only randomly select from the strongest recommendations
    candidate_pool = unique_playlist[:75]

    # Return a different playlist each time
    return random.sample(
        candidate_pool,
        min(number_of_songs, len(candidate_pool))
    )