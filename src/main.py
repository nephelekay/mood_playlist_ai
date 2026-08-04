from track_features import Song, UserProfile
from scoring import score_song


def main():

    test_song = Song(
        track_id="123",
        title="Test Song",
        artists="Test Artist",
        album="Test Album",
        genre="pop",
        mood="Feel-Good",
        energy=0.85,
        tempo=120,
        valence=0.80,
        danceability=0.90,
        acousticness=0.10
    )

    test_user = UserProfile(
        favorite_genres=["pop"],
        favorite_artists=["Test Artist"],
        favorite_moods=["Feel-Good"],

        target_energy=0.80,
        target_tempo=120,
        target_valence=0.75,
        target_danceability=0.85,
        target_acousticness=0.15
    )

    score, reasons = score_song(test_song, test_user)

    print("Score:", score)
    print("Reasons:")

    for reason in reasons:
        print("-", reason)


if __name__ == "__main__":
    main()