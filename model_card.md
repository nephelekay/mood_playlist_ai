# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
MoodPlaylistAI

---

## 2. Intended Use  

This is a music-recommender designed to suggest songs according to the user's preferences. It generates recommendations by comparing the aspects of genre, mood, energy, tempo, valence, danceability, and acousticness.
It assumes the users will enjoy songs similar to their perceived preferences, top three songs, and potentially their favorite artists and genres.

---

## 3. How the Model Works  

The program analyzes several song features, using a scoring algorithm to generate a list of 25 songs with the user's preferences in mind.
Then the program turns these preferences into a score for every song. A song may receive more or less points considering whether they are close to numerical target values, such as energy level or if the song's genre or  artist is in the user's favorite artists or genres.
The starter logic was improved through expanding the dataset to more than 100,000 songs, implementing genre grouping unto the scoring algorithm, adding moood-specific playlist recommendations and producing an html file the user can find spotify links to songs in the playlist.

---

## 4. Data  

The dataset the model uses is from Kaggle. It is comprised of 114,001 Spotify tracks and their respective attributes and information(artists,album, genre, mood, energy, tempo, valence, danceability, and acousticness). The dataset is filtered, eliminating any tracks from language-specific genres as those may actually be of a multitude of genres. Film and broad genres such as sad or groove to make the recommendations more accurate.

---

## 5. Strengths  

The program works well for users with clear preferences, especially based on genre and mood. The scoring system can successfully observe these patterns and offer fitting recommendations. 
The explanations are also helpful as to explain why each was reccomended to the user.

---

## 6. Limitations and Bias 

Unsure what to write here.

---

## 7. Evaluation  

The recommender was tested using several different taste profiles. This allowed to check whether the result matched the expectations of a music recommender. For example, for a pop, happy energy user, one would expect upbeat songs, whereas for a high-energy workout user, one would expect intense songs with fast beat. Say more about the testing

---

## 8. Future Work  

An idea for future improvement is to add a prompt-based recommendation feature where the user can enter a prompt, such as three sentences conveying a melancholic mood and then be presented with a playlist conveying that feeling. This would require building a mini NLP engine. The challenge for this undertaking is selecting an appropriate emotion lexicon/word association dataset and working with that data to make sufficient connections before even reading the user's input.

---

## 9. Personal Reflection  

Throughout this project I gained valuable knowledge on how recommendation systems work. It was very interesting to see how systems turn data into predictions about what users might enjoy. I also learned that it is difficult for a recommendation to be objective, because using a sorting algorithm and a scoring algorithm ensures that it is never truly random. This project helped me understand how real-life platforms like Spotify work in the background to offer recommendations to listeners.
