# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

FaveFinder 1.0  

---

## 2. Intended Use  

This is a music-recommender designed to suggest songs according to the user's preferences. It generates recommendations by comparing the aspects of genre, mood, energy level, and acoustic preference. 
It assumes the users will enjoy songs similar to their perceived preferences. 
It is designed for classroom explorationa and learning rather than real-word users.
The goal of this project is to show how data, comparisons, and scoring comparisons can be used to predict a user's preference and create a test profile. 

---

## 3. How the Model Works  

The program analyzes several aspects, including genre, mood, energy level, and acousticness. The user provides their preferences on those. 
Then the program turns these preferences into a score for every song. A song may receive more or less points caonsidering whether on not they match important preferences.
The starter logic was improved through adding a seighted scoring system instead of simply returning songs in order.

---

## 4. Data  

The dataset the model uses includes a catalog of 20 songs, 9 genres(Pop, Lofi, Rock, Ambient, Jazz, Synthwave, Folk, Electronic, Indie pop), and 8 moods(Happy, Chill, Intense, Relaxed, Focused, Moody, Calm, Inspired). Pars missing from the dataset include lyrics, artist history, user listening behavior, popularity, and cultural influences.

---

## 5. Strengths  

The program works well for users with clear preferences, especially based on genre and mood. The scoring system can successfully observe these patterns and offer fitting recommendations. 
The explanations are also helpful as to explain why each was reccomended to the user.

---

## 6. Limitations and Bias 

The biggest limitation of the program is the use of a small dataset and a limited number of features. The scoring system might also favor certain preferences over others, thus preventing the user from discovering new types of music. Some genres and moods are underrespresented because the dataset is only made up of 20 songs compared to real platforms.

---

## 7. Evaluation  

The recommender was tested using several different taste profiles. This allowed us to check whether the result matched the expectations of a music recommender. For example, for a pop, happy energy user, one would expect upbeat songs, whereas for a high-energy workout user, one would expect intese songs with fast beat.

---

## 8. Future Work  

Some ideas for future improvements are expanding the dataset to include thousands or millions of songs and adding more music features such as instrumentation. Also taking into account user listening history, likes, and skips could work to improve the current design.

---

## 9. Personal Reflection  

Throughout this project I gained valuable knowledge on how recommendation systems work. It was very interesting to see how systems turn data into predictions about what users might enjoy. I also learned that it is difficult for a recommendation to be objective, because using a sorting algorithm and a scoring algorithm ensures that it is never truly random. This project helped me understand how real-life platforms like Spotify work in the background to offer recommendations to listeners.
