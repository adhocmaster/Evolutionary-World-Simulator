# The game of gold hunters

There will be a grid world. Agents need to explore the world and collect golds. Two different strategies:
1. Explore and collect if no one else is around
2. Fight and get gold
3. Escape
4. Share
5. 2, 3, 4 depends on one agent's perception of another agent and their own traits.
6. To make the game more interesting, some agents can dig fast, some agents are better at robbing 
7. The game ends in a restricted number of turns, call it run. Each agent has to maximize their reward. 
8. We will play a series of games, and let agents learn about other agents in phase 2. 
9. How will an agent know if another agent is a digger or a robber.
10. a gold resource has an amount of gold. A digger has a higher speed and efficiency of collecting golds than a robber. Efficiency = % of gold they can collect from a resource.
11. A robber can choose to dig of find a digger and wait for them to dig.
12. There will be many robbers and diggers in the world. 
13. Goals:
    1. Per run: maximum yield per agent, overall production
    2. Evolution: find strategies for each agent that can ensure stability of an optimal production rate. Production rate = total yield per run.

14. Evolution:
    1. Changing strategies,
    2. Optimizing strategies.
    3. A pure robber never digs, a pure digger never fights.
    4. New species emerge as the strategies evolve and traits evolve. We will need some rules of evolution here. 

15. Questions:
    1. Does agents die when they fight?
    2. If all diggers die, the production rate will stablize at the minimum rate. 
    3. Depending on their traits, there should be an optimal share of robbers and diggers. 
    4. Can the diggers notice robbers while digging?
    5. Does robbers take the first action?
    6. How will they navigate in the grid?

16. Utility functions:
    1. UtilityRobber(state, action). Each cell around the robber may have a gold resource, a digger, a robber,  or nothing. If there is a digger(which the robber cannot be sure about), robber has to estimate how much gold can they get from robbery. They can make a prediction based on number of turns played, probability of identifying diggers correctly, 

