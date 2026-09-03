# 🎵 Mood Playlist AI — Personalized Music Recommendation Engine

## Project Summary

Mood Playlist AI is a music recommendation engine that generates personalized song recommendations based on the user's listening preferences.

The project began as a CodePath starter project. I significantly expanded it by replacing the small sample dataset with a dataset of 114,001 Spotify tracks, redesigning the recommendation algorithm around weighted similarity scoring, adding recommendation explanations, generating mood-based playlists, and creating an HTML playlist with clickable Spotify search links.

It compares multiple characteristics of each song to the user's preferences and ranks songs according to their overall similarity.

---

## How The System Works

Every song is represented by several features, including genre, artists, mood, energy, tempo, valence, danceability, and acousticness.

UserProfile stores the user's preferences. The profile is created from at least three of the user's favorite songs and can optionally include their preferred genres and artists. The numerical features of the user's favorite songs are averaged to create target values for the recommendation system.

The personalized playlist creation works as follows:
1. Loads and filters the Spotify dataset.
2. Asks the user for at least three favorite songs and optionally preferred genres and artists to build their profile.
3. Compares each song in the dataset against the preferences stored in the user profile.
4. Uses weighted scoring to determine how close the songs reflect the user's preferences.
5. Ranks songs from highest to lowest score. 
6. Returns 25 highest-scoring recommendations along with explanations as to why each song was recommended.
7. Uses recommendations to create an HTML file with clickable Spotify links to each song.

The mood playlist creation works as follows: 
1. The user selects one of the provided moods. 
2. The system scores each song based on whether it matches the selected mood and whether its genre belongs to an associated mood group.
3. Sorts the matching songs by score and creates a list of the top 75 songs.
4. Randomly selects 25 recommendations from the list.
5. Uses recommendations to create an HTML file with clickable Spotify links to each song.

---

## Recommendation Features

Features considered by the scoring system:
- Genre — rewards songs from genres the user prefers.
- Artist — considers the user's favorite artists.
- Energy — measures how closely the song's energy matches the user's target energy value.
- Tempo — measures similarity between the song's BPM and the user's preferred tempo value.
- Valence — compares the song's emotional tone value.
- Danceability — compares how conducive the song is for dancing.
- Acousticness — compares the user's preference for acoustic versus less acoustic songs.

---

## Mood Classification

Mood Playlist AI assigns each song a mood using its energy, valence, and acousticness values. The classification uses thresholds to place songs into categories such as Acoustic, Party, Dark, Energetic, Feel-Good, Laid-Back, Melancholic, Chill, and Neutral.

---

## Dataset

Mood Playlist AI uses a Kaggle dataset containing 114,001 Spotify tracks. The dataset provides information such as track title, artists, album, genre, energy, tempo, valence, danceability, and acousticness.

The dataset is filtered to remove language-specific and broad genre categories that were less useful for the recommendation system.

---


## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run tests with:

```bash
python -m pytest
```
The test suite checks functionality including mood classification, dataset loading, recommendation ranking, recommendation explanations, duplicate handling, and recommendation limits.

---

## Limitations and Risks

Mood Playlist AI has several limitations. The system relies on a limited set of song features. It does not analyze lyrics, cultural context, listening context, or other information that can affect whether someone enjoys a song.

The weighting of each feature also affects the recommendations. Giving one feature too much weight could cause the system to over-prioritize certain characteristics and reduce the diversity of recommendations or give an advantage to certain genres over others.

---

## Future Improvements

Potential improvements include:
- Prompt-based playlist generation using natural language processing (NLP).
- Incorporating user listening behavior.
- More sophisticated mood and emotion classification.

---

## Reflection

[**Model Card**](model_card.md)

Through this project, I gained a better understanding of how recommendation systems turn data into predictions about what a user might enjoy. I learned how the choice of features, similarity calculations, and weighting can significantly affect the results produced by a recommendation system.

Expanding the original starter project also taught me how to turn a small prototype into a more complete application. I worked with a dataset containing over 114,000 tracks, created a user profile from multiple favorite songs, developed a weighted similarity-based scoring system, implemented related-genre matching, and built separate mood-based playlist generation with HTML and Spotify search links.

I also learned that recommendation systems are not completely objective. The dataset, feature selection, genre classifications, scoring rules, and feature weights all carry bias and influence which artists, genres, and styles are recommended. Thus there is a tradeoff between recommending songs that closely match a user's preferences and exposing them to new music.



