import math
import random
import copy
import numpy

from library.Encounter import Encounter
from library.ResourceType import Resourcetype
from games.GoldHunters.localLib.GHActionType import GHActionType
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent
from games.GoldHunters.localLib.GHAgentType import GHAgentType

# state-less

class GoldHunterEncounter(Encounter):


    def __init__(self):

        self.passiveEncounters = [

            self.collaboration, 
            self.philanthropy, 
            self.competition, 
            self.monopoly, 
            
        ]

        self.robbingEncounters = [

            self.intimidation, 
            self.heist, 
            self.raid

        ]

        self.aggressiveEncounters = [

            self.sabotage, 
            self.combat

        ]

    # TODO combine similarities in the simulate functions
    def simulateAllPassiveEncounters(self, agents, goldResource):

        allChanges = []

        for encounter in self.passiveEncounters:

            testAgents = copy.deepcopy(agents)
            testGoldResource = copy.deepcopy(goldResource)

            
            encounter(testAgents, testGoldResource)

            changes = {goldResource : testGoldResource}

            for i in range(testAgents):

                realAgent = agents[i]
                testAgent = testAgents[i]

                changes[realAgent] = testAgent
            
            allChanges.append(changes)

        return allChanges

    
    def simulateAllAggressiveEncounters(self, agents):

        allChanges = []

        for encounter in self.aggressiveEncounters:

            testAgents = copy.deepcopy(agents)

            encounter(testAgents)

            changes = {}

            for i in range(testAgents):

                realAgent = agents[i]
                testAgent = testAgents[i]

                changes[realAgent] = testAgent

            allChanges.append(changes)

        return allChanges


    def simulateAllRobbingEncounters(self, passiveAgents, aggressiveAgents):

        allChanges = []

        for encounter in self.robbingEncounters:

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

            allChanges.append(changes)

        return allChanges


    def getEncounterResults(self, agents, goldResource = None):
        """
        Simulates the event in which these agents meet.
        Returns the encounter results as a dictionary with original agents as its keys and changed agents as its value.
        """

        passiveAgents = []
        aggressiveAgents = []

        for agent in agents:

            if agent.type == GHAgentType.DIGGER:
                passiveAgents.append(agent)

            elif agent.type == GHAgentType.ROBBER:
                aggressiveAgents.append(agent)

        allEncounterResults = []

        if len(passiveAgents) > 0 and len(aggressiveAgents) > 0:
            allEncounterResults = self.simulateAllRobbingEncounters(passiveAgents, aggressiveAgents)
        
        elif len(passiveAgents) > 0 and goldResource != None:
            allEncounterResults = self.simulateAllPassiveEncounters(passiveAgents, goldResource)

        elif len(aggressiveAgents) > 0:
            allEncounterResults = self.simulateAllAggressiveEncounters(aggressiveAgents)

        strongestAgent = self.getStrongestAgent(agents)
        
        return self.getHighestPayoffEncounter(strongestAgent, allEncounterResults)


    def predictEncounterPayoff(self, agent, nextAction, gridWorld):
        '''Predicts the agent's payoff if the agent takes a certain action'''

        if self.predictPossibleEncounter(agent, nextAction, gridWorld):

            targetLocation = agent.newLocation(agent, nextAction.direction)
            potentialAgents = self.getPotentialEncounterParticipants(targetLocation, gridWorld)
            goldResource = self.getGoldResourceAtLocation(targetLocation, gridWorld)
            
            encounterResults = self.getEncounterResults(potentialAgents, goldResource)

            return self.getPayoffFromEncounterResults(agent, encounterResults)

        return 0


    def getPotentialEncounterParticipants(self, locationOfEncounter, gridWorld):
        """Returns potential agents that could be involved in an encounter at any location."""

        potentialAgents = []

        for xd in range(-1, 2):

            for yd in range(-1, 2):

                inspectingLocation = self.addTuples(locationOfEncounter, (xd, yd))

                potentialAgents.append( gridWorld.getAgentsAtLocation(inspectingLocation) )

        return potentialAgents


    def getHighestPayoffEncounter(self, decidingAgent, allEncounterResults):
        
        bestChanges = {}
        highestGoldDifference = -1 * math.inf
        for encounterResults in allEncounterResults:

            goldDifference = self.getPayoffFromEncounterResults(decidingAgent, encounterResults)

            if goldDifference > highestGoldDifference:

                bestChanges = encounterResults
                highestGoldDifference = goldDifference

        return bestChanges


    def predictPossibleEncounter(self, agent, nextAction, gridWorld):
        """Return whether an agent's action could result in an encounter."""

        targetLocation = agent.aLocationNearby(agent, nextAction.direction)
        potentialParticipants = self.getPotentialEncounterParticipants(targetLocation, gridWorld)

        return len(potentialParticipants) > 1


    def getGoldResourceAtLocation(self, location, gridWorld):

        resourceList = gridWorld.getObjectsAtLocation(location)

        if len(resourceList > 0):
            return resourceList[0]

        else:
            return None

    
    def getPayoffFromEncounterResults(self, agent, encounterResults):

        newGold = encounterResults[agent].getGold()
        return newGold - agent.getGold()

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

        strongestAgent = self.getStrongestAgent(agents)
        agents.remove(strongestAgent)

        goldPrize = 0

        for agent in agents:

            goldLost = math.ceil(agent.getGold() / 2)
            fightingPenalty = math.ceil(strongestAgent.getStrength() / 2)

            agent.removeGold(goldLost + fightingPenalty)
            goldPrize += goldLost
            
        winnerFightingPenalty = math.ceil(self.getAverageStrength(agents) / 3)

        strongestAgent.addGold(goldPrize)
        strongestAgent.removeGold(winnerFightingPenalty)

    # ENCOUNTERS END HERE #

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


    def getStrongestAgent(self, agents):

        agents = sorted(agents, reverse = True, key = self.keyToSortByStrength)
        return agents[0]


    def addTuples(self, tuple1, tuple2):
        return tuple(numpy.add(tuple1, tuple2))


    def getAllEncounters(self):
        return self.passiveEncounters + self.robbingEncounters + self.aggressiveEncounters