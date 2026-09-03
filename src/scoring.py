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
    """Calculates how closely the song's energy matches user's preference.

    Args:
        song: Song object containing energy value.
        user: UserProfile object containing user's target energy.

    Returns:
        Similarity score between 0.0 and 1.0.
    """
    return 1 - abs(song.energy - user.target_energy)


def tempoSimilarityScore(song: Song, user: UserProfile) -> float:
    """Calculates how closely the song's tempo matches user's preference.

    Args:
        song: Song object containing tempo value.
        user: UserProfile object containing user's target tempo.

    Returns:
        Similarity score between 0.0 and 1.0.
    """
    return 1 - abs(song.tempo - user.target_tempo) / 200


def valenceSimilarityScore(song: Song, user: UserProfile) -> float:
    """Calculates how closely the song's valence matches user's preference.

    Args:
        song: Song object containing valence value.
        user: UserProfile object containing user's target valence.

    Returns:
        Similarity score between 0.0 and 1.0.
    """
    return 1 - abs(song.valence - user.target_valence)


def danceabilitySimilarityScore(song: Song, user: UserProfile) -> float:
    """Calculates how closely the song's danceability matches user's preference.

    Args:
        song: Song object containing danceability value.
        user: UserProfile object containing user's target danceability.

    Returns:
        Similarity score between 0.0 and 1.0.
    """
    return 1 - abs(song.danceability - user.target_danceability)


def acousticnessSimilarityScore(song: Song, user: UserProfile) -> float:
    """Calculates how closely the song's acousticness matches user's preference.

    Args:
        song: Song object containing acousticness value.
        user: UserProfile object containing user's target acousticness.

    Returns:
        Similarity score between 0.0 and 1.0.
    """
    return 1 - abs(song.acousticness - user.target_acousticness)


def moodSimilarityScore(song: Song, user: UserProfile) -> float:
    """Checks whether song's mood exists in user's prefered moods.

    Args:
        song: Song object containing mood.
        user: UserProfile object containing the user's favorite moods.

    Returns:
        1.0 if the song's mood is in user's favorite moods, otherwise 0.0.
    """
    if song.mood in user.favorite_moods:
        return 1.0
    else:
        return 0.0

def genreSimilarityScore(song: Song, user: UserProfile) -> float:
    """Calculates genre similarity based on exact and related genre match.

    Exact genre match receives the top score, while genres belonging to
    the same genre group receive a partial score.

    Args:
        song: Song object containing song's genre.
        user: UserProfile object containing user's favorite genres.

    Returns:
        Genre similarity score of 1.0 for exact match, 0.7 for related 
        match, or 0.0 if no match.
    """
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
    """Checks whether song contains artist that is a user's favorite.

    Args:
        song: Song object containing artist.
        user: UserProfile object containing the user's favorite artists.

    Returns:
        1.0 if song includes favorite artist, otherwise 0.0.
    """
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
    """Calculates recommendation score for song.

    Each song feature is compared to user's preferences and multiplied
    by the corresponding weight. Weighted scores are combined to produce
    final score. The three strongest features that contributed produce
    explanations for the recommendation.

    Args:
        song: Song object.
        user: UserProfile object containing user's preferences.

    Returns:
        Tuple containing final score and list of explanations for
        three feautures that most closely matched the user's preferences.
    """
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