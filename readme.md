Civ6 AI Behavior Prediction Model

**Overview**
This repository contains a machine learning model designed to analyze human gameplay in Sid Meier’s Civilization VI using video footage. The video is processed into a series of screenshots, which are analyzed to determine early-game build choices. The goal of this analysis is to predict a set of AI-relevant values, specifically PseudoYields and AiFavoredItems, which influence AI behavior in the game.

By understanding the relationship between human decision-making and AI behavior, this model provides insights that could be used for AI tuning, game balancing, and strategic analysis.

**How It Works**

*Video Processing*

Video footage of Civilization VI gameplay is converted into individual frames.
Key moments (e.g., city founding, unit production, district placement) are extracted for analysis.

*Screenshot Analysis*

Screenshots are processed using image recognition techniques to identify game elements.
The model detects what the player chooses to build in the early game (units, buildings, districts, improvements).
Contextual information (map layout, resources, opponent presence) is also extracted if available.

*Label Prediction*

The extracted data is mapped to a series of pre-labeled values categorized as PseudoYields and AiFavoredItems.
The model is trained to predict these labels based on observed gameplay decisions.

**Key AI-Influencing Labels**

*PseudoYields*

PseudoYields in Civilization VI are internal AI scoring values that determine the desirability of various in-game choices. These scores are influenced by a range of factors, including strategic priorities, resource availability, and opponent behaviors. The model attempts to infer these values based on observed player actions.

*Predictable PseudoYields from Early Gameplay*

City Expansion Priority (e.g., Settler production, tile purchasing)
Military Emphasis (e.g., Training early melee or ranged units, building Encampments)
Scientific Focus (e.g., Prioritizing Campuses, building Libraries early)
Economic Growth (e.g., Emphasizing Commercial Hubs, early gold-generating improvements)
Religious Intent (e.g., Early Holy Sites, shrine construction, faith-based purchases)
Production Efficiency (e.g., Prioritizing Industrial Zones, builders improving high-production tiles)
Diplomatic Weight (e.g., Early Envoy spending, trade route choices, alliances)
Naval Expansion (e.g., Coastal city focus, early galleys, harbors)
The model learns to infer these values based on patterns in player choices. For instance, if a player consistently builds Campuses early, the AI’s PseudoYield_Science might be increased accordingly.

*AiFavoredItems*

AiFavoredItems are specific preferences inserted into the AI decision-making process. These influence how likely the AI is to favor certain builds, policies, wonders, or strategies.

*Potential AiFavoredItems Insertions*

Preferred Districts (e.g., AI may favor Commercial Hubs if early-game gold accumulation is detected)
Wonders & Infrastructure (e.g., If early-game focus on production is observed, AI may prioritize Pyramids or Ruhr Valley)
Unit Composition Bias (e.g., If the player favors cavalry units, the AI may increase its cavalry response)
Technology & Civic Prioritization (e.g., AI might be nudged towards military techs if aggressive early play is detected)
Government Choices (e.g., AI preference for Autocracy over Classical Republic if military-heavy early game is observed)
These preferences help shape AI behavior dynamically based on the observed tendencies of the human player.

This model is an ongoing research project aiming to bridge the gap between human strategic thinking and AI decision-making in Civilization VI. Contributions, suggestions, and insights are welcome! 🚀