import random
from src.track_features import Song, UserProfile
from src.scoring import scoreSong

def recommendSongs( songs: list[Song], user: UserProfile, number_of_songs: int = 25) -> list[tuple[Song, float, list[str]]]:
    recommendations = []

    seen = set()

    for song in songs:
        if song.title in seen: continue
        score_info = scoreSong(song, user)

        score = score_info[0] ##Returns actual score
        reasons = score_info[1] ##Returns reasoning for scoring

        recommendations.append((song, score, reasons))
        seen.add(song.title)

    recommendations.sort(
        key=lambda recommendation: recommendation[1],
        reverse=True
    )

    return recommendations[:number_of_songs] ##Rerurns list of 25 songs(track, score, reasons)

def generateMoodPlaylist(
    songs: list[Song],
    mood: str,
    number_of_songs: int = 25
) -> list[Song]:

    playlist = []

    for song in songs:
        if song.mood.lower() == mood.lower():
            playlist.append(song)

    random.shuffle(playlist)

    return playlist[:number_of_songs]
