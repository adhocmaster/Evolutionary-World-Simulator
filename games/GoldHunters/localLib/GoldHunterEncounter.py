import math
import random
import copy

from library.Encounter import Encounter
from library.ResourceType import Resourcetype
from games.GoldHunters.localLib.GHActionType import GHActionType


class GoldHunterEncounter(Encounter):


    def getTotalMaxGoldPerTurn(self, agents):

        totalMaxGold = 0

        for agent in agents:
            totalMaxGold += agent.getMaxGoldPerTurn()
        
        return totalMaxGold

    
    def getTotalStrength(self, agents):

        totalStrength = 0

        for agent in agents:
            totalStrength += agent.getStrength()

        return totalStrength

    
    def getAverageStrength(self, agents):

        totalStrength = self.getTotalStrength(agents)
        avgStrength = totalStrength / len(agents)
        
        return avgStrength

    
    def getTotalGoldOwned(self, agents):

        totalGold = 0

        for agent in agents:
            totalGold += agent.getGold()
        
        return totalGold


    def keyToSortByGold(self, agent):
        return agent.getGold()

    
    def keyToSortByStrength(self, agent):
        return agent.getStrength()


    def priorityDigging(self, agents, goldResource):
        """Diggers dig once in a set order."""

        totalAmountCollected = 0

        for agent in agents:
            
            amountCollected = agent.dig(goldResource)
            agent.addGold(amountCollected)
            totalAmountCollected += amountCollected
        
        return totalAmountCollected


    def collectiveDigging(self, agents, goldResource):
        """All diggers pool their collections for future distribution."""

        totalAmountCollected = 0

        for agent in agents:

            amountCollected = agent.dig(goldResource)
            totalAmountCollected += amountCollected
        
        return totalAmountCollected

    # ENCOUNTERS START HERE #

    def collaboration(self, agents, goldResource):
        """All agents attempt to dig their max amount and distribute the gold evenly."""
        
        totalAmountCollected = self.collectiveDigging(agents, goldResource)

        goldPerAgent = math.ceil(totalAmountCollected / len(agents))

        for agent in agents:
            agent.addGold(goldPerAgent)

        pass


    def philanthropy(self, agents, goldResource):
        """Agents with less gold dig from the resource first"""

        agents = sorted(agents, reverse = False, key = self.keyToSortByGold)

        self.priorityDigging(agents, goldResource)


    def competition(self, agents, goldResource):
        """Agents gain gold based on their digging rate"""

        totalMaxGold = self.getTotalMaxGoldPerTurn(agents)

        totalAmountCollected = self.collectiveDigging(agents, goldResource)

        for agent in agents:
            agent.addGold(agent.getMaxGoldPerTurn() * totalAmountCollected / totalMaxGold)

        pass


    def monopoly(self, agents, goldResource):
        """Agents with more strength dig from the resource first"""

        agents = sorted(agents, reverse = True, key = self.keyToSortByStrength)

        self.priorityDigging(agents, goldResource)


    def intimidation(self, aggressiveAgents, passiveAgents):
        """Aggressive agents threaten passive agents into giving the gold over."""

        totalAggressiveStrength = self.getTotalStrength(aggressiveAgents)
        totalPassiveStrength = self.getTotalStrength(passiveAgents)

        if totalAggressiveStrength >= totalPassiveStrength * 2:
            
            totalGoldStolen = 0

            for agent in passiveAgents:

                goldStolen = agent.getGold()
                agent.removeGold(goldStolen)
                totalGoldStolen += goldStolen

            for agent in aggressiveAgents:

                goldEarned = math.ceil( totalGoldStolen * (agent.getStrength() / totalAggressiveStrength) )
                agent.addGold(goldEarned)

        else:
            
            penaltyPerAgent = math.ceil(totalPassiveStrength / len(aggressiveAgents))

            for agent in aggressiveAgents:
                agent.removeGold(penaltyPerAgent)

        pass


    def raid(self, aggressiveAgents, passiveAgents):
        """Aggressive agents take turns stealing from passive agents"""

        unrobbedAgents = passiveAgents

        for robber in aggressiveAgents:

            if len(unrobbedAgents) > 0:

                victim = unrobbedAgents[0]
                unrobbedAgents.remove(victim)

                robber.rob(victim)

            else:
                break

        pass


    def heist(self, aggressiveAgents, passiveAgents):
        """Aggressive agents work together to steal from passive agents"""

        totalAggressiveStrength = self.getTotalStrength(aggressiveAgents)
        totalPassiveStrength = self.getTotalStrength(passiveAgents)
        totalGoldOwned = self.getTotalGoldOwned(passiveAgents)

        totalGoldStolen = totalAggressiveStrength - totalPassiveStrength
    
        if totalGoldStolen > 0:

            for agent in passiveAgents:

                goldLost = math.ceil( totalGoldStolen * (agent.getGold() / totalGoldOwned) )
                agent.removeGold(goldLost)
            
            for agent in aggressiveAgents:

                goldStolen = math.ceil( totalGoldStolen * (agent.getStrength() / totalAggressiveStrength) )
                agent.addGold(goldStolen)

        for agent in aggressiveAgents:

            robbingPenalty = math.ceil( (1 - (agent.getStrength() / totalAggressiveStrength)) * totalPassiveStrength )
            agent.removeGold(robbingPenalty)

        pass


    def sabotage(self, agents):
        """Agents attempt to rob each other"""

        for i in range(len(agents)):

            robbingAgent = agents[i]

            victimAgent = agents[0]
            if i < len(agents) - 1:
                victimAgent = agents[i + 1]

            robbingAgent.rob(victimAgent)
            
        pass


    def combat(self, agents):
        """Agents fight each other to get gold, strongest agent gets half of everyone's gold"""

        agents = sorted(agents, reverse = True, key = self.keyToSortByStrength)
        strongestAgent = agents.pop(0)

        goldPrize = 0

        for agent in agents:

            goldLost = math.ceil(agent.getGold() / 2)
            fightingPenalty = math.ceil(strongestAgent.getStrength() / 2)

            agent.removeGold(goldLost + fightingPenalty)
            goldPrize += goldLost
            
        winnerFightingPenalty = math.ceil(self.getAverageStrength(agents) / 3)

        strongestAgent.addGold(goldPrize)
        strongestAgent.removeGold(winnerFightingPenalty)


    def playPassiveEncounter(self, agents, goldResource, encounter):

        testAgents = copy.deepcopy(agents)
        testGoldResource = copy.deepcopy(goldResource)

        encounter(testAgents, testGoldResource)

        changes = {goldResource : testGoldResource}

        for i in range(testAgents):

            realAgent = agents[i]
            testAgent = testAgents[i]

            changes[realAgent] = testAgent

        return changes

    
    def playAggressiveEncounter(self, agents, encounter):

        testAgents = copy.deepcopy(agents)

        encounter(testAgents)

        changes = {}

        for i in range(testAgents):

            realAgent = agents[i]
            testAgent = testAgents[i]

            changes[realAgent] = testAgent

        return changes


    def playDualTypeEncounter(self, passiveAgents, aggressiveAgents, encounter):

        testPassiveAgents = copy.deepcopy(passiveAgents)
        testAggressiveAgents = copy.deepcopy(aggressiveAgents)

        encounter(passiveAgents, aggressiveAgents)

        changes = {}

        allRealAgents = passiveAgents + aggressiveAgents
        allTestAgents = testPassiveAgents + testAggressiveAgents

        for i in range(allTestAgents):

            realAgent = allRealAgents[i]
            testAgent = allTestAgents[i]

            changes[realAgent] = testAgent

        return changes


    def playEncounter(self, encounter, passiveAgents = None, aggressiveAgents = None, goldResource = None):
        """Input passiveAgents and goldResource parameter to indicate passive agent only encounter (diggers).\n
           Input aggressiveAgents parameter to indicate aggresive agent only encounter (robbers).\n
           Input both parameters to indicate dual type encounters (robberies)
           Returns a dictionary with original agents as its keys and changed agents as its value.
        """
        
        if passiveAgents != None and aggressiveAgents != None:
            return self.playDualTypeEncounter(passiveAgents, aggressiveAgents, encounter)
        
        elif passiveAgents != None and goldResource != None:
            return self.playPassiveEncounter(passiveAgents, goldResource, encounter)

        elif aggressiveAgents != None:
            return self.playAggressiveEncounter(aggressiveAgents, encounter)
        
        else:
            return None


    def predictPossibleEncounter(self, agent, nextAction, gridworld):
        # return true or false only. We are predicting that all other agents are gonna move to the cell that this agent would end up in.

        currentLocation = agent.getLocation()

        if nextAction.name == GHActionType.MoveUp:
            # TODO

        pass

    def predictEncounterPayoff(self, agent, nextAction, gridworld):

        # the agent wants to take the nextAction, gridworld represents the world before the turn actually happens. So, there might be some encounters. Predict the encounter and outcome of it.
        
        pass
        