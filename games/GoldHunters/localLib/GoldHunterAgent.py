import math

from library.Agent import Agent
from library.ResourceType import Resourcetype
from library.GridWorld import GridWorld
from games.GoldHunters.localLib.NotFoundInTheWorld import NotFoundInTheWorld


class GoldHunterAgent(Agent):

    # needed properties:
    # 1. diggingRate: maximum amount an agent can dig from the resource
    # 2. efficiency : .8 means it can get a maximum of 80% of the gold collected, discard the other 20%
    # 3. max amount of gold per turn: efficiency * diggingRate.


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


    def getTrait(self):
        return self.getFromOtherProperties('trait')


    def setTrait(self, trait):
        self.setToOtherProperties('trait', trait)


    def getMaxGoldPerTurn(self):
        return math.ceil(self.getEfficiency * self.getDiggingRate)


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
                objects = world.getObjectsAtLocation(currentLocation)
                percievedWorldModel.addToLocation(currentLocation, objects)

        self.setPerceivedWorld( percievedWorldModel )



    def dig(self, goldResource):
        
        amountDug = goldResource.attemptToDig(self.getDiggingRate())
        collectableAmount = math.ceil(amountDug * self.getEfficiency())
        return collectableAmount
    
    
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

        self.percieveWorld(gridworld)

        self.updateStrategy(gridworld)

        self.takeAction(gridworld, encounterEngine)

        pass


    def updateStrategy(self, gridworld):
        pass

    
    def takeAction(self, gridworld, encounterEngine):


        # set nextAction based on strategy and payoff.

        # iterate through the action set.

        trait = self.getTrait()
        percievedWorld = self.getPerceivedWorld()

        # predict encounter payoff
        payoff = {}

        for action in trait.actions:
            if encounterEngine.predictPossibleEncounter(self, action, gridworld):
                payoff[action] = encounterEngine.predictEncounterPayoff(self, action, gridworld)
            else:
                newLocation = self.newLocation(action.direction)
                objectAtLocation = gridworld.getObjectsAtLocation(newLocation)
                payoff[action] = objectAtLocation.value

        return max(payoff, key=payoff.get) # Action with max value.


    def newLocation(self, direction):

        currentLocation = self.getLocation()
        return (currentLocation[0] + direction[0], currentLocation[1] + direction[1])

    