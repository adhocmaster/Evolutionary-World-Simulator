import math, logging
logging.basicConfig(level=logging.DEBUG)

from games.GoldHunters.localLib.GoldResource import GoldResource
from library.GridWorld import GridWorld
from library.ResourceType import ResourceType
from games.GoldHunters.localLib.GHMoveAction import GHMoveAction

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


    def aLocationNearby(self, agent, direction, world):

        currentLocation = agent.getLocation()
        newLocation = (currentLocation[0] + direction[0], currentLocation[1] + direction[1])

        if world.hasLocation(newLocation):
            return newLocation
        
        raise Exception(f"world does not contain {newLocation}")


    def locationByAction(self, agent, nextAction, world):
        """If `nextAction` is a move action, then return the new location. Otherwise, return the original location.
        raises error if the location is invalid"""

        if isinstance(nextAction, GHMoveAction):
            return self.aLocationNearby(agent, nextAction.direction, world)
        return agent.getLocation()


    
    def calculateBounds(self, center, world, perceptionDistance):

        leftBound = max(0, center[0] - perceptionDistance)
        rightBound = min(world.size[0], center[0] + perceptionDistance + 1)
        topBound = max(0, center[1] - perceptionDistance)
        bottomBound = min(world.size[1], center[1] + perceptionDistance + 1)

        return (leftBound, rightBound, topBound, bottomBound)


    def perceiveWorld(self, agent, world):

        location = agent.getLocation()
        perceptionDistance = agent.getPerceptionDistance()

        bounds = self.calculateBounds(location, world, perceptionDistance)

        percievedWorldModel = GridWorld(size = (bounds[1]-bounds[0],  bounds[3]-bounds[2])) # Makes a new world with "radius" of perceptionDistance

        print(f"size of the perceived world: {percievedWorldModel.size}")

        for x in range(bounds[0], bounds[1]): # Spanning the entire diameter.
            for y in range(bounds[2], bounds[3]):
                locationInWorld = (x, y)
                locationInPerceivedWorld = (x - bounds[0], y - bounds[2])

                if world.hasLocation(locationInWorld):
                    agentsAtLocation = world.getAgentsAtLocation(locationInWorld)
                    for agentAtLocation in agentsAtLocation:
                        percievedWorldModel.addAgentToLocation(locationInPerceivedWorld, agentAtLocation)

                    resources = world.getResourcesAtLocation(locationInWorld)
                    for resource in resources:
                        percievedWorldModel.addResourceToLocation(locationInPerceivedWorld, resource)
                else:
                    # TODO, we need to shrink the world? We should have done that earlier when we created the gridworld.
                    pass

        agent.setPerceivedWorld( percievedWorldModel )

    
    def rob(self, robbingAgent, victimAgent):
            
        victimAgentGold = victimAgent.getFromInventory(ResourceType.GOLD)
        quantityToRob = robbingAgent.getStrength() - victimAgent.getStrength()
        robbingPenalty = victimAgent.getStrength()       # the more the victim struggles, the more costly the robbery

        if (quantityToRob > 0):   # cant rob negative amount of gold

            if quantityToRob > victimAgentGold:
                quantityToRob = victimAgentGold
            
            robbingAgent.addGold(quantityToRob)
            victimAgent.removeGold(quantityToRob)
        
        robbingAgent.removeGold(robbingPenalty)


    def takeTurn(self, agent, gridworld, encounterEngine):

        agent.previousGoldOwned.append(agent.getGold())

        if len(agent.previousGoldOwned) > agent.productionHistoryLength:
            agent.previousGoldOwned.pop(0)

        self.perceiveWorld(agent, gridworld)

        self.updateStrategy(agent)

        self.takeAction(agent, gridworld, encounterEngine)

        pass

    
    def updateStrategyProperties(self, agent):

        agent.setEfficiency(agent.type.value['efficiency'])
        agent.setDiggingRate(agent.type.value['diggingRate'])
        agent.setStrength(agent.type.value['strength'])
        pass



    def updateStrategy(self, agent):

        agent.strategy.update(agent)
        pass

    def isActionValid(self, agent, action, world):
        """Invalid conditions:
        1. if location changes, the location must be valid
        2. .... any other conditions goes here
        """

        try:
            _ = self.locationByAction(agent, action, world)
            return True
        except:
            return False



    def takeAction(self, agent, gridworld, encounterEngine):


        # set nextAction based on strategy and payoff.

        # iterate through the action set.
        # predict encounter payoff
        payoff = {}

        for action in agent.actions:

            logging.debug(agent.getLocation())
            logging.debug(action)

            if self.isActionValid(agent, action, gridworld) is False:
                logging.warning(f"invalid action")
                continue

            if encounterEngine.predictPossibleEncounter(agent, action, gridworld):
                payoff[action] = encounterEngine.predictEncounterPayoff(agent, action, gridworld)

            else:

                newLocation = agent.actionsHandler.locationByAction(agent, action, gridworld)
                resources = gridworld.getResourcesAtLocation(newLocation) 
                # How do we define value of a location?
                payoff[action] = agent.actionsHandler.getMaxCollectableFromResources(agent, resources) # the amount of resources the agent can accumulate in 1 turn.

        bestAction = max(payoff, key=payoff.get) # Action with max value.
        agent.setNextAction(bestAction)