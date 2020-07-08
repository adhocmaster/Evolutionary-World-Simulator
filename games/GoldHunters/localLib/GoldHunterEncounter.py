import math
import random

from library.Encounter import Encounter
from library.ResourceType import Resourcetype


class GoldHunterEncounter(Encounter):


    def getTotalMaxGoldPerTurn(self, agents):

        totalMaxGold = 0

        for agent in agents:
            totalMaxGold = agent.getMaxGoldPerTurn()
        
        return totalMaxGold

    
    def getTotalStrength(self, agents):

        totalStrength = 0

        for agent in agents:
            totalStrength += agent.getStrength()

        return totalStrength


    def keyToSortByGold(self, agent):
        return agent.getGold()

    
    def keyToSortByStrength(self, agent):
        return agent.getStrength()


    def priorityDigging(self, agents, goldResource):
        """Diggers dig once in a set order."""

        for agent in agents:
            
            amountCollected = agent.dig(goldResource)
            agent.addGold(amountCollected)
        
        pass


    def collectiveDigging(self, agents, goldResource):
        """All diggers pool their collections for future distribution."""

        totalAmountCollected = 0

        for agent in agents:

            amountCollected = agent.dig(goldResource)
            totalAmountCollected += amountCollected
        
        return totalAmountCollected


    def individualRobbing(self, robbingAgents, victimAgents):

        pass


    def groupRobbing(self, robbingAgents, victimAgents):

        pass


    def collaboration(self, agents, goldResource):
        """All agents attempt to dig their max amount and distribute the gold evenly."""
        
        totalAmountCollected = self.collectiveDigging(agents, goldResource)

        goldPerAgent = math.floor(totalAmountCollected / len(agents))

        for agent in agents:
            agent.addGold(goldPerAgent)

        pass


    def philanthropy(self, agents, goldResource):
        """Agents with less gold dig from the resource first"""

        agents.sort(reverse = False, key = self.keyToSortByGold)

        self.priorityDigging(agents, goldResource)


    def competition(self, agents, goldResource):
        """Agents gain gold based on their digging rate"""

        totalMaxGold = self.getTotalMaxGoldPerTurn(agents)

        totalAmountCollected = self.collectiveDigging(agents, goldResource)

        for agent in agents:
            agent.addGold(self.getMaxGoldPerTurn() * totalAmountCollected / totalMaxGold)

        pass


    def monopoly(self, agents, goldResource):
        """Agents with more strength dig from the resource first"""

        agents.sort(reverse = True, key = self.keyToSortByStrength)

        self.priorityDigging(agents, goldResource)


    def intimidation(self, aggressiveAgents, passiveAgents):
        """Aggressive agents threaten passive agents into giving the gold over."""

        totalAggressiveStrength = self.getTotalStrength(aggressiveAgents)
        totalPassiveStrength = self.getTotalStrength(passiveAgents)

        if totalAggressiveStrength >= totalPassiveStrength * 2:
            # stealing stuff
            pass
        else:
            # get punished
            pass
        pass


    def raid(self, aggressiveAgents, passiveAgents):

        pass


    def heist(self, aggressiveAgents, passiveAgents):

        pass


    def sabotage(self, agents):
        pass


    def combat(self, agents):
        pass
