import math

from library.Agent import Agent
from library.ResourceType import Resourcetype


class GoldHunterAgent(Agent):

    # needed properties:
    # 1. diggingRate: maximum amount an agent can dig from the resource
    # 2. efficiency : .8 means it can get a maximum of 80% of the gold collected, discard the other 20%
    # 3. max amount of gold per turn: efficiency * diggingRate.


    def addGold(self, amount):
        self.addToInventory('gold', amount)


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


    def getMaxGoldPerTurn(self):
        return math.ceil(self.getEfficiency * self.getDiggingRate)


    def getNodeId(self):
        #TODO wait for node implementation
        pass

    
    def moveTo(self, x, y):
        #TODO wait for node implementation
        pass


    def dig(self, goldResource):
        
        amountDug = goldResource.attemptToDig(self.getDiggingRate())
        collectableAmount = math.ceil(amountDug * self.getEfficiency())
        return collectableAmount
    
    
    def rob(self, otherAgent):
            
        otherAgentGold = otherAgent.getFromInventory(Resourcetype.GOLD)
        quantityToRob = self.getStrength() - otherAgent.getStrength()
        RobingPenalty = otherAgent.getStrength()       # the more the victim struggles, the more costly the robbery

        if (quantityToRob > 0):   # cant rob negative amount of gold

            if quantityToRob > otherAgentGold:
                quantityToRob = otherAgentGold
            
            self.addToInventory(Resourcetype.GOLD, quantityToRob)
            otherAgent.removeFromInventory(Resourcetype.GOLD, quantityToRob)
            self.removeFromInventory(Resourcetype.GOLD, RobingPenalty)
