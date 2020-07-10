# Payoff Function

**Payoff Function determines the best place to move given no encounters**

If there are no encounters for the agent, based on its perceived world, the payoff function determines the best move action to execute.

## Steps
- Check for encounters
- If there are none, call the perceive world function
- If payoff for every action is the same, it picks one at random
- Payoff function weights both the quantity of gold and the distance to it through the value of quantity/distance
- Return the location with the max payoff value
- If there is an encounter, return the output of the encounters function
