# Types of Encounters

An encounter is a function that takes in a list of agents and assigns them an action based on its logic and the agents' stats (efficiency, digging rate, strength).

The actions available to the agent:

- Dig
- Rob
- Fight
- Nothing

## Collaboration: Everyone receives the same amount

**When to Trigger -** Multiple passive agents attempt to harvest the same resource.

- All agents add up their potential collection of the resource and attempt to collect that amount.
- All collections will be pooled and distributed evenly.

## Philanthropy: Weighted based on need for resource

**When to Trigger -** Multiple passive agents attempt to harvest the same resource.

- All agents add up their potential collection of the resource and attempt to collect that amount.
- All collections will be pooled and distributed based on how much resource each agent has.
- The less resource an agent has, the more they receive.

## Competition: Weighted based on resource availability

**When to Trigger -** Multiple passive agents attempt to harvest the same resource.

- All agents add up their potential collection of the resource and attempt to collect that amount.
- All collections will be pooled and distributed based on how much each agent dug.

## Monopoly: Strongest dig first

**When to Trigger -** Multiple passive agents attempt to harvest the same resource.

- All agents take turns digging once from the same resource.
- Agents with higher strength dig first.
- If the resource runs out, agents who haven't dug yet get nothing.

## Intimidation : Unconfrontational stealing

**When to Trigger -** Multiple aggressive agents confront multiple passive agents

- If the total strength of the agressive agents is over 2x that of the passive agents, all resources are stolen from the passive agents and distributed to the agressive agents based on their strength.-
 Otherwise, the encounter ends.

## Theft : Confrontational stealing

**When to Trigger -** Multiple aggressive agents confront multiple passive agents

- Aggressive agents take turns attempting to rob a random passive agent once.
- The amount stolen is equal to (robber's strength) - (victim's strength).
- Aggressive agent suffers penalty = victim's strength
- Stronger agents rob first.
- Passive agents can only be robbed once.
- Resources robbed go directly to the agent who stole it.
- If the number of passive agents runs out, the encounter ends.

## Heist : Organized stealing of resources

**When to Trigger -** Multiple aggressive agents confront multiple passive agents

- Ag

## Raid : Unorganized stealing of resources

**When to Trigger -** Multiple aggressive agents confront multiple passive agents

**Result -** 

## Sabotage : Steal each other's resources

**When to Trigger -** Multiple aggressive agents confront each other

 
## Combat : Fight for each other's resources

**When to Trigger -** Multiple aggressive agents confront each other
