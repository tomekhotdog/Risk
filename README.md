# RISK
As is the case for every CS undergrad, it is my duty to breakdown any Christmas boardgame and maximise my chances of consistently beating my brother and sister.

In the game of RISK, players manage the production and movements of their armies so as to gain territories and take over the world. Army production bonuses are earned for holding more territories and continents, and when trading in game cards. Anticipating your enemies' movements and knowing when to launch your assaults is what can win you the war.

### Assaults

Players take control of enemy territories by launching a successful attack, eliminating all the enemy's troops there. An attack is carried out in a series of skirmishes, each with at most 3 attackers and 2 defenders, represented by dice rolls. The highest scores are paired together and survivors established based on the dice scores (with the defender victorious in case of a tie). 

### The Question
Given I have n attackers and I want to attack a territory with m defenders, what is my probability of success? 

The python code simulates repeated skirmishes and prints the probabilities of successful attacks. The following results are based on a Monte Carlo simulation of 100,000 trials.

attackers / defenders 
\~ |~1 ~| ~2 ~ |~ 3 ~ |~ 4 ~ |~ 5 ~ |~ 6 ~ |~ 7 ~ |~ 8 ~ |~9 ~ |~10 ~ |
1  | 0.42 | 0.11 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
2  | 0.76 | 0.36 | 0.21 | 0.09 | 0.05 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 |
3  | 0.91 | 0.66 | 0.47 | 0.31 | 0.21 | 0.14 | 0.08 | 0.05 | 0.03 | 0.02 | 
4  | 0.97 | 0.78 | 0.64 | 0.48 | 0.36 | 0.25 | 0.18 | 0.13 | 0.09 | 0.05 |
5  | 0.99 | 0.89 | 0.76 | 0.64 | 0.52 | 0.40 | 0.30 | 0.22 | 0.16 | 0.11 |
6  | 1.00 | 0.93 | 0.85 | 0.74 | 0.64 | 0.52 | 0.42 | 0.33 | 0.25 | 0.20 |
7  | 1.00 | 0.97 | 0.91 | 0.84 | 0.74 | 0.64 | 0.55 | 0.45 | 0.35 | 0.28 |
8  | 1.00 | 0.98 | 0.95 | 0.89 | 0.82 | 0.74 | 0.65 | 0.55 | 0.47 | 0.38 |
9  | 1.00 | 0.99 | 0.97 | 0.93 | 0.87 | 0.81 | 0.73 | 0.64 | 0.55 | 0.47 |
10 | 1.00 | 0.99 | 0.98 | 0.95 | 0.92 | 0.87 | 0.80 | 0.73 | 0.65 | 0.57 |

If we consider the cases where n equals m (1 vs 1, 2 vs 2, etc.) it is interesting to note that for larger assaults, the attacker has an increasing advantage. The game benefits the attacker launching large scale attacks and this should be incorporated in your strategy.

### Other considerations
There are a few other elements of the game to be considered to perfect the ultimate strategy:
 - Selecting continents to fight for
 - Organisation of troops for attack and defence
 - Saving up game cards
 - Letting enemies weaken each other
 - Coordinating peace treaties with enemies
