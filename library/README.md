# Action Encounter Framework

Reward, u  = f(state, action, encounter) where encounter might be null


# Actions vs PowerActions

Actions are non-encounter actions. When two agents encounters each other, their power actions come into play. We can devise a whole new plan how power actions be simulated. Currently power actions have different kinds of powers and defence against them. So, if an agent has no defence against a power, it loses health.

health = health - power + defense

# Simple simulation of encounters

Iterate through all the power actions of the enemy, update health.