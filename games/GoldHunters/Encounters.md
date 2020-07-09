# Types of Encounters

An encounter is a function that takes in a list of agents and assigns them an action based on its logic and the agents' stats (efficiency, digging rate, strength).

The actions available to the agent:

- Dig
- Rob
- Fight
- Nothing

All calculations for gains and losses are rounded up.

## Collaboration: Everyone receives the same amount

**When to Trigger -** Multiple passive agents attempt to harvest the same resource.

- All agents add up their potential collection of the resource and attempt to collect that amount.
- All collections will be pooled and distributed evenly.

## Philanthropy: Weakest dig first

**When to Trigger -** Multiple passive agents attempt to harvest the same resource.

- All agents take turns digging once from the same resource.
- Agents with lower strength dig first.
- If the resource runs out, the encounter ends.

## Competition: Weighted based on resource availability

**When to Trigger -** Multiple passive agents attempt to harvest the same resource.

- All agents add up their potential collection of the resource and attempt to collect that amount.
- All collections will be pooled and distributed based on how much each agent dug.

## Monopoly: Strongest dig first

**When to Trigger -** Multiple passive agents attempt to harvest the same resource.

- All agents take turns digging once from the same resource.
- Agents with higher strength dig first.
- If the resource runs out, the encounter ends.

## Intimidation : Non-violent stealing

**When to Trigger -** Multiple aggressive agents confront multiple passive agents

- If the total strength of the agressive agents is over 2x that of the passive agents, all resources are stolen from the passive agents and distributed to the aggressive agents based on their strength.
- Otherwise, the aggressive agents collectively suffer a fighting penalty = total passive agents' strength.

## Raid : Unorganized stealing of resources

**When to Trigger -** Multiple aggressive agents confront multiple passive agents

- Aggressive agents take turns attempting to rob a random passive agent once.
- The amount stolen is equal to (robber's strength) - (victim's strength).
- Aggressive agent suffers penalty = victim's strength.
- Stronger agents rob first.
- Passive agents can only be robbed once.
- Resources robbed go directly to the agent who stole it.
- If the number of passive agents runs out, the encounter ends.

## Heist : Organized stealing of resources

**When to Trigger -** Multiple aggressive agents confront multiple passive agents

- The total strength of the aggressive agents is compared to the total strength of the passive agents.
- The amount stolen is equal to (totla robbers' strength) - (total victims' strength).
- Aggressive agents suffers penalty = total victims' strength.
- Aggressive agents collectively steal from the total amount of gold the passive agents have.
- Passive agents suffer losses based on the gold they have, the more gold an agent has, the more they lose.
- Aggressive agents suffer losses based on their strength, the less strength an agent has, the more they lose.
- Aggressive agents gain gold based on their strength, the more strength an agent has, the more they gain.

## Sabotage : Steal each other's resources

**When to Trigger -** Multiple aggressive agents confront each other

- Agents attempt to steal from each other.

## Combat : Fight for each other's resources

**When to Trigger -** Multiple aggressive agents confront each other

- Agents fight each other to take all the others' gold.
- Strongest agent "wins" half of everyone else's gold.
- Winner recieves a fighting penalty = (average strength of other enemies) / 3.
- Everyone else recieves a fighting penalty = (strongest enemy's strength) / 2.
