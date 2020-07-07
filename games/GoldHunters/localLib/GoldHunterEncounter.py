from library.Encounter import Encounter
from library.ResourceType import Resourcetype
import random

class GoldHunterEncounter(Encounter):


    def rob(self, robbingAgents, victimAgents):

        for robbingAgent in robbingAgents:
            
            if len(victimAgents) > 0:
                
                victimAgent = random.choice(victimAgents)
                victimAgents.remove(victimAgent)

                robbingAgent.rob(victimAgent)


    def compete(self, agents):

        for i in range(len(agents)):

            robbingAgent = agents[i]
            victimAgent = agents[0]

            if i < len(agents) - 1:
                victimAgent = agents[i + 1]

            robbingAgent.rob(victimAgent)


    def collaborate(self, agents, resourceToShare):

        originalResourceQuantity = resourceToShare.quantity
        totalDiggingRate = self.getTotalDiggingRate(agents)
        
        for agent in agents:

            quantityToCollect = agent.getMaxGoldPerTurn()

            if totalDiggingRate > originalResourceQuantity:
                quantityToCollect *= originalResourceQuantity / totalDiggingRate

            agent.dig(resourceToShare, quantityToCollect)


    def getTotalDiggingRate(self, agents):

        totalDiggingRate = 0

        for agent in agents:
            totalDiggingRate += agent.getDiggingRate()

        return totalDiggingRate

