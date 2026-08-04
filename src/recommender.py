from src.track_features import Song, UserProfile
from src.scoring import score_song

def recommend_songs( songs: list[Song], user: UserProfile, number_of_songs: int = 25) -> list[tuple[Song, float, list[str]]]:
    recommendations = []

    for song in songs:
        score_info = score_song(song, user)

        score = score_info[0] ##Returns actual score
        reasons = score_info[1] ##Returns reasoning for scoring

        recommendations.append((song, score, reasons))

    recommendations.sort(
        key=lambda recommendation: recommendation[1],
        reverse=True
    )

    return recommendations[:number_of_songs] ##Rerurns list of 25 songs(track, score, reasons)
