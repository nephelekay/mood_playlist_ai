# 🎵 Music Recommender Simulation

## Project Summary

My version takes into account a user profile, and then implements similarity scoring for each song according to the user's preferences. Based on their individual score, songs are sorted. Then the highest scoring songs are returned as recommendations. They are followed by explanations as to why each song was selected.

---

## How The System Works

My design recommends songs by comparing the characterisics of songs based on the user's preferences. Each song stores information about genre, mood etc. The user profile includes information such as favorite genre and mood.
The scores are computed based on how closely they match the user's preferences.To choose a recommendation: 
  1. Consults user profile
  2. Compares preferences with songs
  3. Sorts songs from highest to lowest score
  4. Returns the highest-scored songs
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
python -m pytest
```

---

## Sample Recommendation Output

========== MoodPlaylist AI ==========
1. Build playlist from my favorite songs
2. Generate playlist by mood
3. Exit
Enter your choice (1-3): 1
Loading songs from data/spotify_tracks.csv...
Give me 3 or more favorite songs (separated by commas):calvatore, love,
 video games
Genre + Artists are optional (to skip hit enter)
     What genres do you like? (separate by commas):
    Who are your favorite artists? (separate by commas): 

1. Fui Fiel
Artist: Pablo
Album: Êee Paixão (A Voz Romântica)
Score: 0.787
Reasons:
- Similar energy profile to your favorite tracks
- Similar rhythm and danceability profile
- Similar tempo range to your listening preferences

2. 薄情歌
Artist: C AllStar
Album: CANTOPOPSIBILITY
Score: 0.783
Reasons:
- Similar energy profile to your favorite tracks
- Similar rhythm and danceability profile
- Similar tempo range to your listening preferences

3. I Used To Care
Artist: Louyah
Album: 6FEET
Score: 0.783
Reasons:
- Similar energy profile to your favorite tracks
- Similar rhythm and danceability profile
- Similar tempo range to your listening preferences

4. No One Like You
Artist: Eben;Nathaniel Bassey
Album: No One Like You
Score: 0.783
Reasons:
- Similar energy profile to your favorite tracks
- Similar rhythm and danceability profile
- Similar tempo range to your listening preferences

## Limitations and Risks

There are several limitations to this program, the first being that it is working with a small catalog of songs, therefore, it may not be as accurate as a real platform with millions of songs. The system only considers a few features and does not consider the lyrics, artist popularity, or cultural context which can all influence whether a user enjoys a song or not. Another major limitation is the weighting assigned to each feature. If a genre has a very high weight, then the program may reccomenf only songs from the user's favorite genre and fail to introduce the user to new genres.
---

## Reflection

[**Model Card**](model_card.md)

Through this project, I learned how a platform analyzes data to formulate predictions about what a user might enjoy. More relative to my program, a recomender can analyse genre, mood, energy etc., score them based on similarity, and thus create personalized results. I also investigated how reccomendation systems can contain bias depending on how the scoring is implemented. This would lead to certain artists, genres etc. being favored over others, and limiting users' exposure to new experiences.



