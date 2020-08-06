import math

from library.Agent import Agent
from library.ResourceType import ResourceType
from library.GridWorld import GridWorld
from games.GoldHunters.localLib.GHAgentType import GHAgentType
from games.GoldHunters.localLib.NotFoundInTheWorld import NotFoundInTheWorld
from games.GoldHunters.localLib.GoldResource import GoldResource


class GoldHunterAgent(Agent):

    # needed properties:
    # 1. diggingRate: maximum amount an agent can dig from the resource
    # 2. efficiency : .8 means it can get a maximum of 80% of the gold collected, discard the other 20%
    # 3. max amount of gold per turn: efficiency * diggingRate.


    def __init__(self, type, id, productionHistoryLength, goldQuota, actionsHandler):

        super().__init__(type = type, id = id)

        # Every turn we record the amount of gold the agent accumulated.
        self.previousGoldOwned = []

        # TODO explain how this property is used
        self.productionHistoryLength = productionHistoryLength

        # TODO explain how this property is used
        self.goldQuota = goldQuota

        self.actionsHandler = actionsHandler




    def addGold(self, amount):
        self.addToInventory('gold', amount)


    def removeGold(self, amount):
        self.removeFromInventory('gold', amount)


    def getGold(self):
        return self.getFromInventory('gold')

    
    def setGold(self, amount):
        self.updateInventory('gold', amount)
    

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


    def getResourceStats(self):
        return (
            f"id: {self.id}"
            f"gold: {self.getGold()}"
        )
    