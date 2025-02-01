bmv2 is an unsupervised learning model designed to cluster the build orders, 
settle locations, and other important game behaviours taken by players in 
the game of Civilization V by "Difficulty" / skill level. 

Player behaviour is captured by video and converted to text and labels 
 as player_actions and game_states. The player_actions are described as values in 
the Civilization VI codebase, specifically as values relevant
to the development of game modifications, such as UnitPriorityBoosts in the
AiFavoredItems table, or DefaultImprovements in the AiLists table.

Game_states describe both board features and scores. Board features might
include the turn, the number and location of units and cities, tile yields, 
other players, and the health and movement of units. Scores might include 
culture, science, faith, or gold per turn, era score, military score, or 
food, population, and production.

Once trained, bmv2 model will be able to cluster player_actions features by 
score, offering a way to show 