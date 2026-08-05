from src.recommender import Song, UserProfile, Recommender, scoreSong

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""

def test_recommendation_changes_for_different_user_preferences():
    """
    A lofi/chill user should receive the lofi song as the top recommendation.
    """
    user = UserProfile(
        favorite_genre="lofi",
        favorite_mood="chill",
        target_energy=0.4,
        likes_acoustic=True,
    )

    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert results[0].genre == "lofi"
    assert results[0].mood == "chill"


def test_energy_similarity_affects_score():
    """
    Songs with energy closer to the user's target should receive higher scores.
    """
    user = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.8,
        "likes_acoustic": False,
    }

    high_energy_song = {
        "genre": "jazz",
        "mood": "relaxed",
        "energy": 0.8,
        "acousticness": 0.5,
    }

    low_energy_song = {
        "genre": "jazz",
        "mood": "relaxed",
        "energy": 0.2,
        "acousticness": 0.5,
    }

    high_score, _ = scoreSong(user, high_energy_song)
    low_score, _ = scoreSong(user, low_energy_song)

    assert high_score > low_score


def test_acoustic_preference_affects_score():
    """
    Users who prefer acoustic songs should score acoustic songs higher.
    """
    user = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.5,
        "likes_acoustic": True,
    }

    acoustic_song = {
        "genre": "jazz",
        "mood": "relaxed",
        "energy": 0.5,
        "acousticness": 0.9,
    }

    electronic_song = {
        "genre": "jazz",
        "mood": "relaxed",
        "energy": 0.5,
        "acousticness": 0.1,
    }

    acoustic_score, _ = scoreSong(user, acoustic_song)
    electronic_score, _ = scoreSong(user, electronic_song)

    assert acoustic_score > electronic_score
