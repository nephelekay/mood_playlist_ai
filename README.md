# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

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
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:
Loading songs from data/songs.csv...

=== Top 5 Music Recommendations ===

1. Weekend Escape by Coastal Waves
   Genre: pop | Mood: happy
   Score: 69.85
   Reasons: Genre match (+30), Mood match (+20), Energy similarity (+14.8), Low acousticness (+5)
--------------------------------------------------

2. Sunrise City by Neon Echo
   Genre: pop | Mood: happy
   Score: 69.70
   Reasons: Genre match (+30), Mood match (+20), Energy similarity (+14.7), Low acousticness (+5)
--------------------------------------------------

3. Gym Hero by Max Pulse
   Genre: pop | Mood: intense
   Score: 64.05
   Reasons: Genre match (+30), Energy similarity (+13.1), Low acousticness (+5)
--------------------------------------------------

4. Rooftop Lights by Indigo Parade
   Genre: indie pop | Mood: happy
   Score: 39.40
   Reasons: Mood match (+20), Energy similarity (+14.4), Low acousticness (+5)
--------------------------------------------------

5. City Pulse by Voltage Avenue
   Genre: electronic | Mood: energetic
   Score: 17.65
   Reasons: Energy similarity (+13.3), Low acousticness (+5)
--------------------------------------------------
```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
taste_profile = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.40,
    "target_tempo": 80,
    "target_valence": 0.60,
    "target_danceability": 0.60,
    "target_acousticness": 0.75
}


**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->
Loading songs from data/songs.csv...

=== Top 5 Music Recommendations ===

1. Weekend Escape by Coastal Waves
   Genre: pop | Mood: happy
   Score: 69.85
   Reasons: Genre match (+30), Mood match (+20), Energy similarity (+14.8), Low acousticness (+5)
--------------------------------------------------
2. Sunrise City by Neon Echo
   Genre: pop | Mood: happy
   Score: 69.70
   Reasons: Genre match (+30), Mood match (+20), Energy similarity (+14.7), Low acousticness (+5)
--------------------------------------------------
3. Gym Hero by Max Pulse
   Genre: pop | Mood: intense
   Score: 48.05
   Reasons: Genre match (+30), Energy similarity (+13.1), Low acousticness (+5)
--------------------------------------------------
4. Rooftop Lights by Indigo Parade
   Genre: indie pop | Mood: happy
   Score: 39.40
   Reasons: Mood match (+20), Energy similarity (+14.4), Low acousticness (+5)
--------------------------------------------------
5. Night Drive Loop by Neon Echo
   Genre: synthwave | Mood: moody
   Score: 19.25
   Reasons: Energy similarity (+14.2), Low acousticness (+5)
--------------------------------------------------

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- When I lowered the weight of the genre, it made the genre a less important factor in the recommendation score. The program stopped prioritizxing whether a song belongs to the user's favorite genre and relied more on other aspects like mood, energy etc.
- When I added tempo to the score it helped to distinguish between slow and faster songs. This allowed the recommender to become more detailed and accurate, as it considered more aspects about the song's sound. A user that might prefer relaxing music with a slower tempo would be recommended songs of similar tempos.
- The program produced different recommendations depending on each user's preferences. Someone who likes high-energy pop pieces would be recommended more pop songs, happy mood songs, and energetic beats. On the contrary, someone who likes more relaxed, study-type pieces, would likely be recommended lofi or ambient music.

---

## Limitations and Risks

Summarize some limitations of your recommender.

There are several limitations to this program, the first being that it is working with a small catalog of songs, therefore, it may not be as accurate as a real platform with millions of songs. The system only considers a few features and does not consider the lyrics, artist popularity, or cultural contesxt which can all influence whether a user enjoys a song or not. Another major limitation is the weighting assigned to each feature. If a genre has a very high weight, then the program may reccomenf only songs from the user's favorite genre and fail to introduce the user to new genres.
---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Through this project, I learned how a platform analyzes data to formulate predictions about what a user might enjoy. More relative to my program, a recomender can analyse genre, mood, energy etc., score them based on similarity, and thus create personalized results. I also investigated how reccomendation systems can contain bias depending on how the scoring is implemented. This would lead to certain artists, genres etc. being favored over others, and limiting users' exposure to new experiences.



