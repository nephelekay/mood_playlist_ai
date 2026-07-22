# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I aksed the agent to help me build, understand and improve the music recommender system. The goal was to implement the given functions in a way that simulates real platforms and learn the fundamentals behind the data structures needed to bring this program to life.

**Prompts used:**
I prompted the agent several times, but one of the prompts I used was this:
Give me different ideas on how to calculate a score for energy (it is a numeric value), rewarding songs closer to the user's preferences, instead of just having a higher or lower score. Explain the advantages and disadvantages of each. 

**What did the agent generate or change?**
The agent recommended a higher scoring penalty for genre and mood. This makes sense, as one usually listens to music based on their mood. Also genre and mood are heavily intertwined.

**What did you verify or fix manually?**

I verified that the scoring made sense and tweaked the scoring regarding energy.
---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

My design depended on breaking up the program into different parts, verifying that they worked, before moving on to the next. I followed closely the instructions in the project description.

**How did AI help you brainstorm or implement it?**

I prompted AI regarding each small part without changing too much at once. I made small changes, tested them, and then once I knew they worked well, moved on to the next.

**How does the pattern appear in your final code?**

This pattern can be seen in how the program handles the recommendations. There is a separation between the scoring and the actual recommendation. That is the score_song() function explicitly handles scoring, and then it is called by the reccomend_songs() function.