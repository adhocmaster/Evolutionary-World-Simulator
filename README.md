# Action Encounter Framework

Reward, u  = f(state, action, encounter) where encounter might be null


# Actions vs PowerActions

Actions are non-encounter actions. When two agents encounters each other, their power actions come into play. We can devise a whole new plan how power actions be simulated. Currently power actions have different kinds of powers and defence against them. So, if an agent has no defence against an offensive, it loses health.

health = health - power + defense

## Move Action
Different species move in different speed. So, each move action needs to define the speed at which an agent can move. In a grid world the unit is a cell.

# Simple simulation of encounters

Iterate through all the power actions of the enemy, update health.

# Factories

## ActionFactory

The most important methods are to create random actions.

## TraitFactory

The most important methods are to create random traits. There is a caveat, in a map-based game, there might be some movements that's common to everyone, and some not. There can be even a group of movements that needs to be present together. Right now we will only think of two generic kinds of agents:

1. Agents that can move, like rabbits
2. Agents that cannot move, like plants


## How do we model population capacity?

1 tiger = 5 rabbits or 1 tiger = 1 rabbit. Maybe we can device a plan on normalized population shares. So, every agent needs to have a normalization factor.

## Resources

How much value can someone get from a resource.
Both agents and the world can have resources. There are two types of resources: depletable, non-depletable. We don't let resource to have a life. So, plants can grow resources, but the nutritions can't. Can we model **world cells** as agents, too?

## Cost of encounters

Instead of defining cost in terms of value, we model deaths and injuries. How do they recover? 

1. Contribution to self, world, and other agents.
2. encounter strategies
3. Each encounter needs to be a custom function because it's too complicated to model it.


# Encounter Map
Plants cannot encounter animals. But they can consume resources available in the world. 

# Big Challenges:

1. Resource growth: Maybe growth rate per turn based on available resources and health of the agent. 
2. Payoff: Payoffs are actually contributions towards shares. Because we are only interested in shares.
3. Reproduction: when and how fast an agent can reproduce? Do they need to mate? Can mating can be modeled as a collaboration?
4. Age: age should be in numbers of turns. 
5. Movement speed.
6. Can agents change their strategy?


# Agents
Agents cannot change their strategy? Because agents are strategies. Or should we model strategies seperately and at any point agent shares denote strategy shares? If we model strategy seperately, there can be interesting results.

## Properties
Name | Type | Required | Purpose
--- | --- | --- | ---
id | any | yes | Uniquely identifies each agent. 
type | string | yes | This is the strategy. In a HD game, types would be Hawk and Dove


# Perceptions
Now comes the hardest part. How do we model perceptions and perception strategies?

1. Perception of resources
2. Perception of need
3. Perception of other agents
4. How doe perception evolves? Evolution of perception? Where is the limitation of EvG?+

