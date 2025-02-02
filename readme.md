Civ6 AI Behavior Prediction Model

**Overview**

Welcome to Buddy Model, version 2! Bm-v2 is an engine that attempts to use human gameplay in Sid Meier’s Civilization VI to improve AI behaviour in-game.

**Ambition: Making a mod**

Ultimately our goal is a mod manipulating an in-game variable called "PseudoYields". These (we think) define the internal value Civ VI AIs assign to various in-game choices. There are PseudoYields for many specific units, buildings, districts, improvements, and wonders -- maybe all of them. 

In bm-v2, we focus only on influencing the PseudoYields of specific buildings, using the build orders of the players we are analysing to attempt to infer the value a human player playing at a high difficulty level would have.

**How It Works**

Bm-v2 takes video footage of people playing Civilization VI and converts it into images and then text, capturing the build decisions of the player and converting them into sequences. Once completed, these are fed back into the LLM again to form a prediction for the PseudoYield value of each building and unit, and finally this is fed in one more time to generate a mod.

*Success and failure*

In bm-v2 we have no idea whether our model or the mods it leads to actually improve the AI's performance, but in future iterations our intention is too additional capture game states in the image analysis phase, and use that to compare the performance of Prince AIs in our mod versus those in the base game.  

**Towards a real model**

Ultimately, our ambition with buddy model is to use the images, video, and text data that can be generated from people's play to create game code. Using the raw information of images, multimedia, and rich text, it should be possible to specifically predict: 

- individual structured outputs, such as the specific float values of each PseudoYield
- mod code, transformed from a semantic descriptions of human gameplay
- "good" and "bad" play, reinforced using the scoring systems built into the game itself

...and much more! This is a work in progress, we've got a long way to go.