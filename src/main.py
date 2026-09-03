
from src.track_features import loadSongs, createUserProfile
from src.playlist import recommendSongs, generateMoodPlaylist
from src.html_output import createPlaylistHTML


def main():
    """Runs main menu for the MoodPlaylist AI application.
    Provides options to build profile-based recommendation playlist, generate
    playlist matched to a specific mood, or exit program.
    """
    print("========== MoodPlaylist AI ==========")
    print("1. Build playlist from my favorite songs")
    print("2. Generate playlist by mood")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")

    if choice == "1": # Profile-based recommendations
        songs = loadSongs("data/spotify_tracks.csv")
        user = createUserProfile(songs)

        recommendations = recommendSongs(songs, user, 25) # Get top 25 recommended tracks matching profile
        createPlaylistHTML(recommendations)
        printRecommended(recommendations)

    elif choice == "2": # Mood-based recommendations
        print("---------------------------------------")
        print("Generate a playlist based on your mood:")
        print("Acoustic    Party     Dark     Energetic")
        print("Feel-Good  Laid-Back  Melancholic  Chill")
        mood = input("Enter your choice:")
        songs = loadSongs("data/spotify_tracks.csv") # Load data and filter tracks matching user's mood
        recommendations = generateMoodPlaylist(songs, mood, 25)
        createPlaylistHTML(recommendations) # Export playlist to HTML and print summary to console
        printRecommended(recommendations)
    
   

def printRecommended(recommend_tracks):
    """Formats and prints recommended tracks to console.

    Args:
        recommend_tracks: List of tuples, where each tuple contains
            (song_object, score_float, reasons_list).
    """
    number = 1
    # Print track metadata, matching score, and explanation reasons
    for track in recommend_tracks:
        song = track[0]
        score = track[1]
        reasons = track[2]

        print(f"\n{number}. {song.title}")
        print(f"Artist: {song.artists}")
        print(f"Album: {song.album}")
        print(f"Score: {score:.3f}")

        print("Reasons:")
        for reason in reasons:
            print("-", reason)

        number += 1



if __name__ == "__main__":
    main()