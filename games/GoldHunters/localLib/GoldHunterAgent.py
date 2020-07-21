import math

from library.Agent import Agent
from library.ResourceType import Resourcetype
from library.GridWorld import GridWorld
from games.GoldHunters.localLib.GHAgentType import GHAgentType
from games.GoldHunters.localLib.NotFoundInTheWorld import NotFoundInTheWorld
from games.GoldHunters.localLib.GoldResource import GoldResource


class GoldHunterAgent(Agent):

    # needed properties:
    # 1. diggingRate: maximum amount an agent can dig from the resource
    # 2. efficiency : .8 means it can get a maximum of 80% of the gold collected, discard the other 20%
    # 3. max amount of gold per turn: efficiency * diggingRate.


    def __init__(self, type, id, productionHistoryLength, goldQuota):

        super().__init__(type = type, id = id)

        # Every turn we record the amount of gold the agent accumulated.
        self.previousGoldOwned = []

        # TODO explain how this property is used
        self.productionHistoryLength = productionHistoryLength

        # TODO explain how this property is used
        self.goldQuota = goldQuota


    def addGold(self, amount):
        self.addToInventory('gold', amount)


    def removeGold(self, amount):
        self.removeFromInventory('gold', amount)


    def getGold(self):
        return self.getFromInventory('gold')
    

    def getEfficiency(self):
        return self.getFromOtherProperties('efficiency')
    

    def setEfficiency(self, efficiency):
        self.setToOtherProperties('efficiency', efficiency)


    def getDiggingRate(self):
        return self.getFromOtherProperties('diggingRate')


    def setDiggingRate(self, diggingRate):
        self.setToOtherProperties('diggingRate', diggingRate)


    def getStrength(self):
        return self.getFromOtherProperties('strength')


    def setStrength(self, strength):
        self.setToOtherProperties('strength', strength)


    def getPerceivedWorld(self):
        return self.getFromOtherProperties('perceivedWorld')


    def setPerceivedWorld(self, perceivedWorld):
        self.setToOtherProperties('perceivedWorld', perceivedWorld)


    def getNextAction(self):
        return self.getFromOtherProperties('nextAction')


    def setNextAction(self, nextAction):
        self.setToOtherProperties('nextAction', nextAction)


    def getMaxGoldPerTurn(self):
        return math.ceil(self.getEfficiency() * self.getDiggingRate())


    def getNodeId(self):
        #TODO wait for node implementation
        pass

    
    def updateAgentLocation(self, location):
        #TODO wait for node implementation
        self.setToOtherProperties("location", location)
        pass

    
    def getLocation(self):
        try:
            return self.getFromOtherProperties("location")
        except:
            raise NotFoundInTheWorld(f"agent {self.id} not found in the world.")
    
    
    def getPerceptionDistance(self):
        return self.getFromOtherProperties('perceptionDistance')

    
    def setPerceptionDistance(self, perceptionDistance):
        self.setToOtherProperties('perceptionDistance', perceptionDistance)


    def percieveWorld(self, world):

        location = self.getLocation()
        perceptionDistance = self.getPerceptionDistance()
        percievedWorldModel = GridWorld(size = perceptionDistance * 2) # Makes a new world with "radius" of perceptionDistance

        for x in range(location[0], location[0] + 2 * perceptionDistance): # Spanning the entire diameter.
            for y in range(location[1], location[1] + 2 * perceptionDistance):
                currentLocation = [x, y]
                agents = world.getAgentsAtLocation(currentLocation)
                percievedWorldModel.addAgentToLocation(currentLocation, agents)
                resources = world.getResourcesAtLocation(currentLocation)
                percievedWorldModel.addResourceToLocation(currentLocation, resources)

        self.setPerceivedWorld( percievedWorldModel )


    def dig(self, resource):
        
        amountDug = resource.amountPerDig(self.getDiggingRate())
        resource.dig(amountDug)
        collectableAmount = math.ceil(amountDug * self.getEfficiency())
        return collectableAmount
        

    def getMaxCollectableFromResource(self, goldResource):
        
        amountDug = goldResource.amountPerDig(self.getDiggingRate())
        collectableAmount = math.ceil(amountDug * self.getEfficiency())
        return collectableAmount

    
    def getMaxCollectableFromResources(self, resources):

        amount = 0
        maxAmount = self.getDiggingRate() * self.getEfficiency()

        for resource in resources:
            if isinstance(resource, GoldResource):
                amountFromThisResource = resource.amountPerDig(self.getDiggingRate())
                if amount + amountFromThisResource <= maxAmount:
                    amount = amount + amountFromThisResource

        return amount


    
    
    def rob(self, otherAgent):
            
        otherAgentGold = otherAgent.getFromInventory(Resourcetype.GOLD)
        quantityToRob = self.getStrength() - otherAgent.getStrength()
        robbingPenalty = otherAgent.getStrength()       # the more the victim struggles, the more costly the robbery

        if (quantityToRob > 0):   # cant rob negative amount of gold

            if quantityToRob > otherAgentGold:
                quantityToRob = otherAgentGold
            
            self.addGold(quantityToRob)
            otherAgent.removeGold(quantityToRob)
        
        self.removeGold(robbingPenalty)


    def takeTurn(self, gridworld, encounterEngine):

        self.previousGoldOwned.append(self.getGold())

        if len(self.previousGoldOwned) > self.productionHistoryLength:
            self.previousGoldOwned.pop(0)

        self.percieveWorld(gridworld)

        self.updateStrategy()

        self.takeAction(gridworld, encounterEngine)

        pass

    
    def updateStrategyProperties(self):

        self.setEfficiency(self.type['efficiency'])
        self.setDiggingRate(self.type['diggingRate'])
        self.setStrength(self.type['strength'])
        pass



    def updateStrategy(self):

        self.strategy.update(self)
        pass

    
    def takeAction(self, gridworld, encounterEngine):


        # set nextAction based on strategy and payoff.

        # iterate through the action set.
        # predict encounter payoff
        payoff = {}

        for action in self.actions:

            if encounterEngine.predictPossibleEncounter(self, action, gridworld):
                payoff[action] = encounterEngine.predictEncounterPayoff(self, action, gridworld)

            else:

                newLocation = self.aLocationNearby(action.direction)
                resources = gridworld.getResourcesAtLocation(newLocation) 
                # How do we define value of a location?
                payoff[action] = self.getMaxCollectableFromResources(resources) # the amount of resources the agent can accumulate in 1 turn.

        bestAction = max(payoff, key=payoff.get) # Action with max value.
        self.setNextAction(bestAction)


    # TODO the name is confusing. 
    def aLocationNearby(self, direction):

        currentLocation = self.getLocation()
        return (currentLocation[0] + direction[0], currentLocation[1] + direction[1])

    