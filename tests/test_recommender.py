from src.track_features import generateMood, loadSongs, createUserProfile
from src.playlist import recommendSongs
from src.track_features import UserProfile

def test_generate_happy_party_mood():
    mood = generateMood(
        energy=0.9,
        valence=0.85,
        acousticness=0.1
    )

    assert mood == "Party"


def test_generate_acoustic_mood():
    mood = generateMood(
        energy=0.3,
        valence=0.5,
        acousticness=0.9
    )

    assert mood == "Acoustic"


def test_load_songs():
    songs = loadSongs("data/spotify_tracks.csv")

    assert len(songs) > 0
    assert songs[0].title != ""
    assert isinstance(songs[0].energy, float)

def test_recommendations_return_25():
    songs = loadSongs("data/spotify_tracks.csv")

    user = UserProfile(
        favorite_genres=["pop"],
        favorite_artists=["Taylor Swift"],
        favorite_moods=["Feel-Good"],
        target_energy=0.7,
        target_tempo=120,
        target_valence=0.8,
        target_danceability=0.7,
        target_acousticness=0.3
    )

    recommendations = recommendSongs(
        songs,
        user,
        25
    )

    assert len(recommendations) <= 25