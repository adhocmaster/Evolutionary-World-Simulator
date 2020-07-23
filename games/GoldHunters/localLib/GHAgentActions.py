import math
from games.GoldHunters.localLib.GoldResource import GoldResource
from games.GoldHunters.localLib.GridWorld import GridWorld
from library.ResourceType import ResourceType

class GHAgentActions:

    def dig(self, agent, resource):
        
        amountDug = resource.amountPerDig(agent.getDiggingRate())
        resource.deplete(amountDug)
        collectableAmount = math.ceil(amountDug * agent.getEfficiency())
        return collectableAmount


    def getMaxCollectableFromResource(self, agent, goldResource):
        
        amountDug = goldResource.amountPerDig(agent.getDiggingRate())
        collectableAmount = math.ceil(amountDug * agent.getEfficiency())
        return collectableAmount

    
    def getMaxCollectableFromResources(self, agent, resources):

        amount = 0
        maxAmount = agent.getDiggingRate() * agent.getEfficiency()

        for resource in resources:
            if isinstance(resource, GoldResource):
                amountFromThisResource = resource.amountPerDig(agent.getDiggingRate())
                if amount + amountFromThisResource <= maxAmount:
                    amount = amount + amountFromThisResource

        return amount


    
    def aLocationNearby(self, agent, direction):

        currentLocation = agent.getLocation()
        return (currentLocation[0] + direction[0], currentLocation[1] + direction[1])

    def percieveWorld(self, agent, world):

        location = agent.getLocation()
        perceptionDistance = agent.getPerceptionDistance()
        percievedWorldModel = GridWorld(size = perceptionDistance * (1, 1)) # Makes a new world with "radius" of perceptionDistance

        print(f"size of the perceived world: {percievedWorldModel.size}")

        for x in range(location[0], location[0] + perceptionDistance + 1): # Spanning the entire diameter.
            for y in range(location[1], location[1] + perceptionDistance + 1):
                locationInWorld = (x, y)
                locationInPerceivedWorld = (x - location[0], y - location[1])

                if world.hasLocation(locationInWorld):
                    agents = world.getAgentsAtLocation(locationInWorld)
                    percievedWorldModel.addAgentToLocation(locationInPerceivedWorld, agents)
                    resources = world.getResourcesAtLocation(locationInWorld)
                    percievedWorldModel.addResourceToLocation(locationInPerceivedWorld, resources)

        agent.setPerceivedWorld( percievedWorldModel )

    
    def rob(self, agent, otherAgent):
            
        otherAgentGold = otherAgent.getFromInventory(ResourceType.GOLD)
        quantityToRob = agent.getStrength() - otherAgent.getStrength()
        robbingPenalty = otherAgent.getStrength()       # the more the victim struggles, the more costly the robbery

        if (quantityToRob > 0):   # cant rob negative amount of gold

            if quantityToRob > otherAgentGold:
                quantityToRob = otherAgentGold
            
            agent.addGold(quantityToRob)
            otherAgent.removeGold(quantityToRob)
        
        agent.removeGold(robbingPenalty)


    def takeTurn(self, agent, gridworld, encounterEngine):

        agent.previousGoldOwned.append(agent.getGold())

        if len(agent.previousGoldOwned) > agent.productionHistoryLength:
            agent.previousGoldOwned.pop(0)

        agent.percieveWorld(gridworld)

        self.updateStrategy(agent)

        self.takeAction(agent, gridworld, encounterEngine)

        pass

    
    def updateStrategyProperties(self, agent):

        agent.setEfficiency(agent.type['efficiency'])
        agent.setDiggingRate(agent.type['diggingRate'])
        agent.setStrength(agent.type['strength'])
        pass



    def updateStrategy(self, agent):

        agent.strategy.update(agent)
        pass

    
    def takeAction(self, agent, gridworld, encounterEngine):


        # set nextAction based on strategy and payoff.

        # iterate through the action set.
        # predict encounter payoff
        payoff = {}

        for action in agent.actions:

            if encounterEngine.predictPossibleEncounter(agent, action, gridworld):
                payoff[action] = encounterEngine.predictEncounterPayoff(agent, action, gridworld)

            else:

                newLocation = agent.actionsHandler.aLocationNearby(action.direction)
                resources = gridworld.getResourcesAtLocation(newLocation) 
                # How do we define value of a location?
                payoff[action] = agent.actionsHandler.getMaxCollectableFromResources(resources) # the amount of resources the agent can accumulate in 1 turn.

        bestAction = max(payoff, key=payoff.get) # Action with max value.
        agent.setNextAction(bestAction)