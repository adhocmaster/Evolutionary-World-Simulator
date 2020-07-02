from library.Encounter import Encounter
from library.ResourceType import Resourcetype

class GoldHunterEncounter(Encounter):

    def __init__(self, agents, resourceToShare):

        self.agents = agents
        self.resourceToShare = resourceToShare


    def compete(self):
        #TODO implement compete method
        pass


    def collaborate(self):

        originalResourceQuantity = self.resourceToShare.quantity
        totalDiggingRate = self.getTotalDiggingRate()
        
        for agent in self.agents:

            quantityToCollect = agent.getMaxGoldPerTurn()

            if totalDiggingRate > originalResourceQuantity:
                quantityToCollect *= originalResourceQuantity / totalDiggingRate

            agent.dig(self.resourceToShare, quantityToCollect)


    def getTotalDiggingRate(self):

        totalDiggingRate = 0

        for agent in self.agents:
            
            totalDiggingRate += agent.getDiggingRate()

        return totalDiggingRate

