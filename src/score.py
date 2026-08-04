from src.track_elements import Song, UserProfile

##Scoring per category.
ENERGY_WEIGHT = 0.22
DANCEABILITY_WEIGHT = 0.18
VALENCE_WEIGHT = 0.14
TEMPO_WEIGHT = 0.14
ACOUSTICNESS_WEIGHT = 0.12
GENRE_WEIGHT = 0.12
ARTIST_WEIGHT = 0.08

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

def energy_similarity_score(song: Song, user: UserProfile) -> float:
    return 1 - abs(song.energy - user.target_energy)


def tempo_similarity_score(song: Song, user: UserProfile) -> float:
    return 1 - abs(song.tempo - user.target_tempo) / 200


def valence_similarity_score(song: Song, user: UserProfile) -> float:
    return 1 - abs(song.valence - user.target_valence)


def danceability_similarity_score(song: Song, user: UserProfile) -> float:
    return 1 - abs(song.danceability - user.target_danceability)


def acousticness_similarity_score(song: Song, user: UserProfile) -> float:
    return 1 - abs(song.acousticness - user.target_acousticness)


def mood_similarity_score(song: Song, user: UserProfile) -> float:
    if song.mood in user.favorite_moods:
        return 1.0
    else:
        return 0.0

def genre_similarity_score(song: Song, user: UserProfile) -> float:
    if song.genre in user.favorite_genres:
        return 1.0
    else:
        return 0.0

def artist_similarity_score(song: Song, user: UserProfile) -> float:
    if song.artists in user.favorite_artists:
        return 1.0
    else:
        return 0.0
    
def score_song(song: Song, user: UserProfile) -> tuple[float, list[str]]:
    score_features = {
        "energy": energy_similarity_score(song, user) * ENERGY_WEIGHT,
        "danceability": danceability_similarity_score(song, user) * DANCEABILITY_WEIGHT,
        "valence": valence_similarity_score(song, user) * VALENCE_WEIGHT,
        "tempo": tempo_similarity_score(song, user) * TEMPO_WEIGHT,
        "acousticness": acousticness_similarity_score(song, user) * ACOUSTICNESS_WEIGHT,
        "genre": genre_similarity_score(song, user) * GENRE_WEIGHT,
        "artist": artist_similarity_score(song, user) * ARTIST_WEIGHT
    }

    top_features = sorted(score_features, key=score_features.get, reverse=True)[:3]

    reasons = []

    for feature in top_features:
        reasons.append(FEATURE_EXPLANATIONS[feature])

    score = sum(score_features.values())

    return score, reasons

