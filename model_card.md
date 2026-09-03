# 🎧 Model Card: Mood Playlist AI

## 1. Model Name  

Mood Playlist AI

---

## 2. Intended Use  

Mood Playlist AI is a content-based music recommendation system designed to suggest songs based on a user's listening preferences.

The system assumes that songs with similar characteristics to a user's favorite songs are more likely to be enjoyable to that user.

The system is intended to provide music recommendations and is not designed to replace professional music recommendation platforms.

---

## 3. Design Approach  

The recommendation system uses a content-based approach. A user's profile is built from their favorite songs, and the system uses the characteristics of those songs to establish their preferences. Individual characteristics are then given different weights when determining how closely another song matches the profile.

The mood playlist feature uses a different approach. It uses manually defined rules to classify songs into moods and identify songs that fit a selected mood.


---

## 4. Strengths  

One of the main strengths of the system is that its recommendations are explainable. Rather than producing a recommendation without context, the system identifies the features that contributed most to its score.

The system is also relatively easy to modify. The scoring weights, genre relationships, and mood rules are explicitly defined, so they can be adjusted without retraining a model.

Another strength is that the system can represent different types of preferences. A user may prefer a particular genre, artist, energy level, tempo, or combination of these characteristics rather than relying on a single preference.


---

## 5. Limitations and Bias 
The biggest limitation is that musical preference cannot be completely represented by numerical audio features. Two songs can have similar energy, tempo, or valence while still sounding very different. The system does not account for lyrics, songwriting, cultural context, personal associations, or the situation in which a song is being played.

The mood classifications are also subjective. The thresholds used to assign moods were manually chosen, so a song classified as Melancholic or Chill, for example, may not be perceived that way by every listener.

The recommendation weights introduce another source of bias. Giving genre or energy more influence than other features means that the system will favor those characteristics when making recommendations. These weights reflect design decisions rather than learned evidence about what users actually prefer.

The genre groupings can introduce similar bias. Treating certain genres as related may produce useful recommendations, but those relationships are subjective and may not reflect how every listener categorizes music.

---

## 6. Evaluation  

The automated tests verify that important parts of the system behave as expected, including mood classification, dataset loading, recommendation ordering, recommendation explanations, duplicate handling, and song limits.

The recommendation output was also inspected using example user profiles to determine whether the results were reasonable given the preferences provided.


---

## 7. Future Work  

A major area for future development would be incorporating natural-language input. For example, a user could describe a desired playlist as "something melancholic for a rainy evening" instead of selecting a predefined mood.

The system could also be improved by making mood classification more sophisticated and introducing mechanisms that balance similarity with recommendation diversity.

---

## 8. Personal Reflection  

One of the most important things I learned from this project is that building a recommendation system involves more than simply finding similar data. The decisions about which features to use, how those features are weighted, and how relationships between categories are defined all influence the final result.

Expanding the original CodePath project gave me the opportunity to make those design decisions myself and see how they affected the behavior of the system. It also showed me the importance of evaluating the assumptions behind a recommendation system rather than only evaluating whether the code runs correctly.