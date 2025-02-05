# Tutorial on Representing Priority Scores for Buildings and Units in Civilization VI

This tutorial explores different methods for representing and calculating the priority scores of buildings and units in Civilization VI, based on the frequency and order in which they are chosen during gameplay. We will dive into the following methods:

1. **Frequency-Based Weighting**
2. **Order-Based Value (Time-Weighted)**
3. **Hybrid Model (Frequency + Time)**
4. **Priority Rank (Ranking Systems)**

Additionally, we will provide an in-depth look at **Weighted Averages**, **Rank Ordering**, **Pareto Efficiency**, **MCDA (Multi-Criteria Decision Analysis)**, and **MAUT (Multi-Attribute Utility Theory)** for effectively managing priority scores.

## 1. Frequency-Based Weighting

### Overview
In this method, we assume that the more often a building or unit is selected, the higher its perceived value. By counting the frequency of each choice across all cities and games, we can assign a higher priority to more frequently chosen units and buildings.

### How to Implement:
1. **Count** how many times each building/unit is chosen in the dataset.
2. **Normalize** the frequency counts (e.g., by dividing by the total number of build decisions made).
3. **Assign Priority Score** based on normalized counts.

### Example:
- Building A: Chosen 30 times in 50 decisions → Frequency score = 30 / 50 = 0.6
- Building B: Chosen 10 times in 50 decisions → Frequency score = 10 / 50 = 0.2

### Use Case:
This method is useful when the priority is directly tied to how often a player builds a specific building/unit.

---

## 2. Order-Based Value (Time-Weighted)

### Overview
This method weights decisions based on their **order in the sequence** of builds. The earlier a building/unit is selected, the more weight it gets, since early decisions are often more strategic or influential.

### How to Implement:
1. **Assign a weight** to each build decision that decays with time (e.g., exponential decay).
2. **Sum** these weighted values for each building/unit to calculate the total priority.

### Example Decay Function (Exponential Decay):
- Decay formula: `score = Σ(1 / e^position)`, where `position` is the order of the build decision.
  
For a building chosen at position 1 (early), the weight will be higher than a building chosen at position 10 (later).

### Use Case:
This approach works when early decisions are considered to have more value than later ones in the game.

---

## 3. Hybrid Model (Frequency + Time)

### Overview
This model combines both frequency-based weighting and time-based (order) weighting to capture both how often something is built and when it is built in the game's timeline.

### How to Implement:
1. **Calculate Frequency Score**: As described in Method 1.
2. **Calculate Time-Weighted Score**: As described in Method 2.
3. **Combine Scores**: Use a weighted average to combine the two scores into a final priority score. 

### Example:

priority_score = α * frequency_score + β * time_weighted_score

Where `α` and `β` are constants to adjust the importance of frequency versus time.

### Use Case:
This model is ideal when both the frequency and the timing of a choice contribute to its importance.

---

## 4. Priority Rank (Ranking Systems)

### Overview
In this method, we assign a **rank** to each building/unit based on the order it is selected in the build sequence. The lower the rank (i.e., the earlier it is chosen), the higher its priority.

### How to Implement:
1. **Rank the choices** based on their position in the build order.
2. **Inverse Rank**: Assign higher priority to lower ranks, e.g., rank 1 → priority 1, rank 2 → priority 0.5, rank 3 → priority 0.33, etc.

### Example:
- Building A: Rank 1 → Priority 1
- Building B: Rank 3 → Priority 0.33

### Use Case:
This approach is useful when you want a discrete ranking system where the order of selection is the key factor.

---

# Deeper Dive into Mathematical Tools

## Weighted Averaging

### What is Weighted Averaging?
A **weighted average** is a type of average where each value in the dataset is given a weight based on its importance. This is useful when some values (such as frequency or time) should contribute more to the final score than others.

### How to Use:
1. Multiply each value by its corresponding weight.
2. Sum the weighted values.
3. Divide by the sum of the weights.

### Example:

weighted_average = (value1 * weight1 + value2 * weight2 + ...) / (weight1 + weight2 + ...)


### Best Practices:
- **Normalization**: Ensure the weights are normalized so that they sum to 1 for a balanced contribution.
- **Context**: Adjust the weights based on the importance of each factor in your context (e.g., prioritize early builds over frequency).

---

## Rank Ordering

### What is Rank Ordering?
**Rank ordering** is the process of assigning a rank to each item based on its position in a sorted list. In our case, we rank buildings and units based on when they are chosen.

### Best Practices:
- **Inverse Rank**: Consider using inverse rank, where rank 1 gets the highest score, rank 2 gets the next, and so on. This method prioritizes earlier selections.
- **Tied Ranks**: If multiple items share the same rank, you can average their positions or assign them a shared rank.

---

# Advanced Concepts: Pareto Efficiency, MCDA, and MAUT

### Pareto Efficiency
**Pareto Efficiency** refers to a state where no individual or preference can be made better off without making someone else worse off. In the context of prioritization, you may want to ensure that no decision can be made without negatively impacting the overall system.

### How to Use:
- Apply **Pareto Analysis** to identify the most beneficial buildings or units that can be prioritized without harming other game aspects.

### Resources:
- "Pareto Analysis for Decision Making" by Philip J. Fleming
- Websites on **Pareto Improvement** and **Pareto Frontiers**.

---

### Multi-Criteria Decision Analysis (MCDA)
**MCDA** is a method used to evaluate and compare different options based on multiple criteria. In your case, this would allow you to compare buildings/units across several dimensions like frequency, timing, and strategic importance.

### How to Use:
1. Define criteria (e.g., frequency, time).
2. Assign scores for each criterion.
3. Use a decision matrix to evaluate and compare options.

### Resources:
- "Multiple Criteria Decision Analysis: State of the Art Surveys" by Alessio Ishizaka
- Online courses and guides on **MCDA tools**.

---

### Multi-Attribute Utility Theory (MAUT)
**MAUT** is a more sophisticated approach to decision-making that incorporates multiple attributes, each weighted according to its importance. MAUT assigns a utility value to each option, allowing comparison across different criteria.

### How to Use:
1. Define the attributes (e.g., frequency, time, game impact).
2. Assign utility values to each option.
3. Calculate the weighted sum to get an overall utility score.

### Resources:
- "Multiattribute Decision Making: Methods and Applications" by E. K. Wong
- Online tutorials on **MAUT** and **utility theory**.

# MAUT and Utility Theory Resources

## 1. Multi-Attribute Utility Theory (MAUT)

- **[Understanding MAUT](https://www.d-sight.com/utility-maut?utm_source=chatgpt.com)**: This article provides a comprehensive overview of MAUT, explaining its key components and how it aids in decision-making by evaluating and ranking alternatives based on multiple attributes.
  
- **[ResearchGate Paper on MAUT](https://www.researchgate.net/publication/226468665_The_Multi-attribute_Utility_Method?utm_source=chatgpt.com)**: This research paper delves into the methodology of MAUT, offering insights into its application in various decision-making scenarios.

- **[FasterCapital's Guide on MAUT](https://www.fastercapital.com/technology/multi-attribute-utility-theory.html?utm_source=chatgpt.com)**: This guide explores the power of MAUT in decision analysis, detailing its steps and applications in evaluating alternatives.

## 2. Utility Theory

- **[Khan Academy's Introduction to Utility](https://www.khanacademy.org/economics-finance-domain/ap-microeconomics/basic-economic-concepts/cost-benefit-analysis/v/introduction-to-utility?utm_source=chatgpt.com)**: This video introduces the concept of utility in economics, explaining how it measures the usefulness or value of something and its role in decision-making.

- **[Scaler Topics on Utility Theory in AI](https://www.scaler.com/topics/artificial-intelligence-tutorial/utility-theory-in-artificial-intelligence/?utm_source=chatgpt.com)**: This article discusses how utility theory is applied in artificial intelligence, allowing AI systems to make decisions based on perceived value and preferences.

- **[TutorialsPoint on Utility Theory and Decision Analysis](https://www.tutorialspoint.com/utility-theory-and-decision-analysis?utm_source=chatgpt.com)**: This tutorial covers the basics of utility theory and its application in decision analysis, providing a foundation for understanding how decisions are made under uncertainty.

## 3. Additional Resources

- **[MIT's Lecture on Expected Utility Theory](https://ocw.mit.edu/courses/14-121-microeconomic-theory-i-fall-2015/2cdfea3bb4b483f46c573a5a2ed4cc1d_MIT14_121F15_5S.pdf?utm_source=chatgpt.com)**: This lecture provides an in-depth look at expected utility theory, discussing its principles and applications in economic decision-making.

- **[Open University's Guide on Making Decisions](https://www.open.edu/openlearn/money-business/leadership-management/making-decisions/content-section-3.2?utm_source=chatgpt.com)**: This resource outlines the decision-making process, including the role of utility theory in evaluating alternatives and making informed choices.

## 4. Video Resource

- **[Multi-Attribute Utility Analysis Video](https://www.youtube.com/watch?pp=ygUQI21vZGVsX2F0dHJpYnV0ZQ%3D%3D&v=R2gitGhqL5o&utm_source=chatgpt.com)**: This video provides a visual explanation of Multi-Attribute Utility Analysis, which can be helpful for understanding how MAUT works in practice.

