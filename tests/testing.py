from src.track_features import generateMood, loadSongs
from src.playlist import recommendSongs
from src.track_features import UserProfile

#Example user profile
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
# Test mood assignment based on features
def test_generate_happy_party_mood():
    mood = generateMood(energy=0.9, valence=0.85, acousticness=0.1)
    assert mood == "Party"

def test_generate_acoustic_mood():
    mood = generateMood(energy=0.3, valence=0.5, acousticness=0.9)
    assert mood == "Acoustic"

def test_generate_dark_mood(): 
    mood = generateMood( energy=0.85, valence=0.2, acousticness=0.1 ) 
    assert mood == "Dark" 
    
def test_generate_energetic_mood(): 
    mood = generateMood( energy=0.8, valence=0.5, acousticness=0.3 ) 
    assert mood == "Energetic" 
    
def test_generate_feel_good_mood(): 
    mood = generateMood( energy=0.6, valence=0.8, acousticness=0.2 ) 
    assert mood == "Feel-Good" 
    
def test_generate_chill_mood(): 
    mood = generateMood( energy=0.3, valence=0.3, acousticness=0.2 ) 
    assert mood == "Chill"

#Test songs loaded correctly
def test_load_songs():
    songs = loadSongs("data/spotify_tracks.csv")

    assert len(songs) > 0
    assert songs[0].title != ""
    assert isinstance(songs[0].energy, float)

#Test recommendations are in descending score order
def test_recommendations_are_sorted_by_score():
    songs = loadSongs("data/spotify_tracks.csv")
    recommendations = recommendSongs(songs, user, 25)
    scores = [score for song, score, reasons in recommendations]

    assert scores == sorted(scores, reverse=True)

#Ensure each reccomendation has at least one explanation
def test_recommendations_have_reasons():
    songs = loadSongs("data/spotify_tracks.csv")
    recommendations = recommendSongs(songs, user, 25)

    for song, score, reasons in recommendations:
        assert len(reasons) > 0

#Test recommended list does not contain exact duplicates of songs
def test_recommendations_have_no_duplicate_titles():
    songs = loadSongs("data/spotify_tracks.csv")
    recommendations = recommendSongs(songs, user, 25)
    titles = [song.title.lower() for song, score, reasons in recommendations]

    assert len(titles) == len(set(titles))

#Test that playlist adheres to song limit
def test_recommendations_return_25():
    songs = loadSongs("data/spotify_tracks.csv")
    recommendations = recommendSongs(songs, user, 25)

    assert len(recommendations) <= 25

