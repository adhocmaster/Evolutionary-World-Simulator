from library.Encounter import Encounter
from library.ResourceType import Resourcetype
import math

class GoldHunterEncounter(Encounter):

    def __init__(self, agents, resourceToShare):

        self.agents = agents
        self.resourceToShare = resourceToShare


    def compete(self):

        pass


    def collaborate(self):

        originalResourceQuantity = self.resourceToShare.quantity
        
        totalDiggingRate = self.getTotalDiggingRate()
        
        for agent in self.agents:

            agentEfficiency = agent.otherProperties['efficiency']
            agentDiggingRate = agent.otherProperties['diggingRate']

            if totalDiggingRate > originalResourceQuantity:
                agentDiggingRate *= originalResourceQuantity / totalDiggingRate
            
            quantityToCollect  = math.floor(agentEfficiency * agentDiggingRate)

            agent.addToInventory(Resourcetype.GOLD, quantityToCollect)
            self.resourceToShare.dec(quantityToCollect)


    def getTotalDiggingRate(self):

        totalDiggingRate = 0

        for agent in self.agents:
            
            totalDiggingRate += agent.otherProperties['diggingRate']

        return totalDiggingRate

