
from src.track_features import loadSongs, createUserProfile
from src.playlist import recommendSongs, generateMoodPlaylist, recommendPromptSongs



def main():
    print("========== MoodPlaylist AI ==========")
    print("1. Build playlist from my favorite songs")
    print("2. Generate playlist by mood")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        songs = loadSongs("data/spotify_tracks.csv")
        user = createUserProfile(songs)

        recommendations = recommendSongs(songs, user, 25)
        printRecommended(recommendations)

    if choice == "2":
        print("---------------------------------------")
        print("Generate a playlist based on your mood:")
        print("Acoustic    Party     Dark     Energetic")
        print("Feel-Good  Laid-Back  Melancholic  Chill")
        mood = input("Enter your choice:")
        generateMoodPlaylist(mood)
        recommendations = generateMoodPlaylist(mood)
        printRecommended(recommendations)
    
   

def printRecommended(recommend_tracks):
    number = 1

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