from src.track_features import Song, UserProfile

##Scoring per category.
ENERGY_WEIGHT = 0.20
DANCEABILITY_WEIGHT = 0.16
VALENCE_WEIGHT = 0.13
TEMPO_WEIGHT = 0.13
ACOUSTICNESS_WEIGHT = 0.12
GENRE_WEIGHT = 0.20
ARTIST_WEIGHT = 0.06

##Explanations to recommendations.
FEATURE_EXPLANATIONS = {
    "energy": "Similar energy profile to your favorite tracks",
    "danceability": "Similar rhythm and danceability profile",
    "valence": "Similar emotional feel to songs you enjoy",
    "tempo": "Similar tempo range to your listening preferences",
    "acousticness": "Similar acoustic style to your favorite tracks",
    "genre": "Matches genres found in your listening history",
    "artist": "Related to artists you already enjoy"
}

##Genre groups.
GENRE_GROUPS = [
    {
        "metal",
        "heavy-metal",
        "death-metal",
        "black-metal",
        "metalcore",
        "hard-rock"
    },
    {
        "rock",
        "alt-rock",
        "alternative",
        "hard-rock",
        "grunge",
        "psych-rock",
        "rock-n-roll",
        "rockabilly"
    },
    {
        "punk",
        "punk-rock",
        "hardcore",
        "emo"
    },
    {
        "pop",
        "indie-pop",
        "power-pop",
        "synth-pop"
    }
]

def energySimilarityScore(song: Song, user: UserProfile) -> float:
    return 1 - abs(song.energy - user.target_energy)


def tempoSimilarityScore(song: Song, user: UserProfile) -> float:
    return 1 - abs(song.tempo - user.target_tempo) / 200


def valenceSimilarityScore(song: Song, user: UserProfile) -> float:
    return 1 - abs(song.valence - user.target_valence)


def danceabilitySimilarityScore(song: Song, user: UserProfile) -> float:
    return 1 - abs(song.danceability - user.target_danceability)


def acousticnessSimilarityScore(song: Song, user: UserProfile) -> float:
    return 1 - abs(song.acousticness - user.target_acousticness)


def moodSimilarityScore(song: Song, user: UserProfile) -> float:
    if song.mood in user.favorite_moods:
        return 1.0
    else:
        return 0.0

def genreSimilarityScore(song: Song, user: UserProfile) -> float:
    song_genre = song.genre.lower()
    favorite_genres = [
        genre.lower()
        for genre in user.favorite_genres
    ]

    # Exact match
    if song_genre in favorite_genres:
        return 1.0

    # Related match
    for genre_group in GENRE_GROUPS:
        if song_genre in genre_group:
            if any(
                favorite_genre in genre_group
                for favorite_genre in favorite_genres
            ):
                return 0.7

    return 0.0

def artistSimilarityScore(song: Song, user: UserProfile) -> float:
    song_artists = [
        artist.strip().lower()
        for artist in song.artists.split(";")
    ]

    favorite_artists = [
        artist.lower()
        for artist in user.favorite_artists
    ]

    if any(artist in favorite_artists for artist in song_artists):
        return 1.0

    return 0.0
    
def scoreSong(song: Song, user: UserProfile) -> tuple[float, list[str]]:
    score_features = {
        "energy": energySimilarityScore(song, user) * ENERGY_WEIGHT,
        "danceability": danceabilitySimilarityScore(song, user) * DANCEABILITY_WEIGHT,
        "valence": valenceSimilarityScore(song, user) * VALENCE_WEIGHT,
        "tempo": tempoSimilarityScore(song, user) * TEMPO_WEIGHT,
        "acousticness": acousticnessSimilarityScore(song, user) * ACOUSTICNESS_WEIGHT,
        "genre": genreSimilarityScore(song, user) * GENRE_WEIGHT,
        "artist": artistSimilarityScore(song, user) * ARTIST_WEIGHT
    }

    top_features = sorted(score_features, key=score_features.get, reverse=True)[:3]

    reasons = []

    for feature in top_features:
        reasons.append(FEATURE_EXPLANATIONS[feature])

    score = sum(score_features.values())

    return score, reasons


def scorePromptSong(song: Song, user: UserProfile):

    score = 0

    if song.mood in user.favorite_moods:
        score += 0.70

    score += valenceSimilarityScore(song, user) * 0.20
    score += energySimilarityScore(song, user) * 0.10

    return score
