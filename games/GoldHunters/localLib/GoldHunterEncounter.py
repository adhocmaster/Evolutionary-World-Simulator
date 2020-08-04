import math
import random
import copy
import numpy

import logging

from library.Encounter import Encounter
from library.ResourceType import ResourceType
from games.GoldHunters.localLib.GHActionType import GHActionType
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent
from games.GoldHunters.localLib.GHAgentType import GHAgentType
from games.GoldHunters.localLib.GHAgentActions import GHAgentActions
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory

# state-less

class GoldHunterEncounter(Encounter):


    def __init__(self, actionsHandler = None, agentFactory = None):

        if actionsHandler is None:
            print("Warning: creating the default actionsHandler")
            # raise Exception("GHAgentFactory needs an actionsHandler.")
            self.actionsHandler = GHAgentActions()
        else:
            self.actionsHandler = actionsHandler

        if agentFactory is None:
            print("Warning: creating the default agentFactory")
            # raise Exception("GHAgentFactory needs an agentFactory.")
            self.agentFactory = GHAgentFactory()
        else:
            self.agentFactory = agentFactory


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


    def simulateAllPassiveEncounters(self, agents, goldResource):
        return self.simulateMultipleEncounters(self.passiveEncounters, passiveAgents = agents, goldResource = goldResource)

    
    def simulateAllAggressiveEncounters(self, agents):
        return self.simulateMultipleEncounters(self.aggressiveEncounters, aggressiveAgents = agents)


    def simulateAllRobbingEncounters(self, passiveAgents, aggressiveAgents):
        return self.simulateMultipleEncounters(self.robbingEncounters, passiveAgents = passiveAgents, aggressiveAgents = aggressiveAgents)


    def simulateMultipleEncounters(self, encounters, goldResource = None, **kwargs):
        '''
        kwargs: passiveAgents, aggressiveAgents, goldResource
        '''

        allChanges = []

        for encounter in encounters:
            
            allRealAgents = []
            allSimulatedAgents = []

            kwargsForEncounter = {}

            goldResourceCopy = None
            if goldResource != None:

                goldResourceCopy = copy.deepcopy(goldResource)
                
                allRealAgents.append(goldResource)
                allSimulatedAgents.append(goldResourceCopy)

            for agentType, agents in kwargs.items():

                allRealAgents.extend(agents)

                simulatedAgents = self.agentFactory.copyAgents(agents)
                kwargsForEncounter[agentType] = simulatedAgents
                allSimulatedAgents.extend(simulatedAgents)

            changes = {}

            encounter(goldResource = goldResourceCopy, **kwargsForEncounter)

            for i in range(len(allRealAgents)):

                realAgent = allRealAgents[i]
                simulatedAgent = allSimulatedAgents[i]

                changes[realAgent] = simulatedAgent

            allChanges.append(changes)

        return allChanges

        

    def getEncounterResults(self, agents, goldResource = None):
        """
        Simulates the event in which these agents meet at a single location.
        Returns the encounter results as a dictionary with original agents/resources as its keys and changed agents/resources as its value.
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
            
            # currentLocation = agent.getLocation()
            targetLocation = agent.actionsHandler.locationByAction(agent, nextAction, gridWorld)
            
            potentialAgents = self.getPotentialEncounterParticipants(targetLocation, gridWorld)
            goldResource = self.getGoldResourceAtLocation(targetLocation, gridWorld)
            
            encounterResults = self.getEncounterResults(potentialAgents, goldResource)

            return self.getPayoffFromEncounterResults(agent, encounterResults)

        return 0


    def predictPossibleEncounter(self, agent, nextAction, gridWorld):
        """Return whether an agent's action could result in an encounter."""

        targetLocation = agent.actionsHandler.locationByAction(agent, nextAction, gridWorld)

        potentialParticipants = self.getPotentialEncounterParticipants(targetLocation, gridWorld)

        return len(potentialParticipants) > 1


    def getPossibleNearbyLocations(self, locationOfEncounter, gridWorld):

        locations = []

        for xd in range(-1, 2):
            for yd in range(-1, 2):
                inspectingLocation = self.addTuples(locationOfEncounter, (xd, yd))
                if gridWorld.hasLocation(inspectingLocation):
                    locations.append(inspectingLocation)

        return locations



    def getPotentialEncounterParticipants(self, locationOfEncounter, gridWorld):
        """Returns potential agents that could be involved in an encounter at any location."""

        potentialAgents = []

        possibleNearbyLocations = self.getPossibleNearbyLocations(locationOfEncounter, gridWorld)

        for inspectingLocation in possibleNearbyLocations:

            logging.debug(f"inspectingLocation: {inspectingLocation}")
            potentialAgents.extend( gridWorld.getAgentsAtLocation(inspectingLocation) )

        return potentialAgents


    def getGoldResourceAtLocation(self, location, gridWorld):

        resourceList = gridWorld.getResourcesAtLocation(location)

        if len(resourceList) > 0:
            return resourceList[0]

        else:
            return None


    def getHighestPayoffEncounter(self, decidingAgent, allEncounterResults):
        
        bestChanges = {}
        highestGoldDifference = -1 * math.inf
        for encounterResults in allEncounterResults:

            goldDifference = self.getPayoffFromEncounterResults(decidingAgent, encounterResults)

            if goldDifference > highestGoldDifference:

                bestChanges = encounterResults
                highestGoldDifference = goldDifference

        return bestChanges

    
    def getPayoffFromEncounterResults(self, agent, encounterResults):

        newGold = encounterResults[agent].getGold()
        return newGold - agent.getGold()

    # ENCOUNTERS START HERE #

    def collaboration(self, goldResource, **kwargs):
        """All agents attempt to dig their max amount and distribute the gold evenly."""

        agents = kwargs.get('passiveAgents')
        
        totalAmountCollected = self.collectiveDigging(agents, goldResource)

        goldPerAgent = math.ceil(totalAmountCollected / len(agents))

        for agent in agents:
            agent.addGold(goldPerAgent)

        pass


    def philanthropy(self, goldResource, **kwargs):
        """Agents with less gold dig from the resource first"""

        agents = kwargs.get('passiveAgents')

        agents = sorted(agents, reverse = False, key = self.keyToSortByGold)

        self.priorityDigging(agents, goldResource)


    def competition(self, goldResource, **kwargs):
        """Agents gain gold based on their digging rate"""

        agents = kwargs.get('passiveAgents')

        totalMaxGold = self.getTotalMaxGoldPerTurn(agents)

        totalAmountCollected = self.collectiveDigging(agents, goldResource)

        for agent in agents:
            agent.addGold(math.ceil(agent.getMaxGoldPerTurn() * totalAmountCollected / totalMaxGold))

        pass


    def monopoly(self, goldResource, **kwargs):
        """Agents with more strength dig from the resource first"""

        agents = kwargs.get('passiveAgents')

        agents = sorted(agents, reverse = True, key = self.keyToSortByStrength)

        self.priorityDigging(agents, goldResource)


    def intimidation(self, **kwargs):
        """Aggressive agents threaten passive agents into giving the gold over."""

        passiveAgents = kwargs.get('passiveAgents')
        aggressiveAgents = kwargs.get('aggressiveAgents')

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


    def raid(self, **kwargs):
        """Aggressive agents take turns stealing from passive agents"""

        passiveAgents = kwargs.get('passiveAgents')
        aggressiveAgents = kwargs.get('aggressiveAgents')

        unrobbedAgents = passiveAgents

        for robber in aggressiveAgents:

            if len(unrobbedAgents) > 0:

                victim = unrobbedAgents[0]
                unrobbedAgents.remove(victim)

                self.actionsHandler.rob(robber, victim)

            else:
                break

        pass


    def heist(self, **kwargs):
        """Aggressive agents work together to steal from passive agents"""

        passiveAgents = kwargs.get('passiveAgents')
        aggressiveAgents = kwargs.get('aggressiveAgents')

        totalAggressiveStrength = self.getTotalStrength(aggressiveAgents)
        totalPassiveStrength = self.getTotalStrength(passiveAgents)
        totalGoldOwned = self.getTotalGoldOwned(passiveAgents)

        totalGoldStolen = totalAggressiveStrength - totalPassiveStrength
    
        if totalGoldStolen > 0 and totalGoldOwned > 0:

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


    def sabotage(self, **kwargs):
        """Agents attempt to rob each other"""

        agents = kwargs.get('aggressiveAgents')

        for i in range(len(agents)):

            robbingAgent = agents[i]

            victimAgent = agents[0]
            if i < len(agents) - 1:
                victimAgent = agents[i + 1]

            self.actionsHandler.rob(robbingAgent, victimAgent)
            
        pass


    def combat(self, **kwargs):
        """Agents fight each other to get gold, strongest agent gets half of everyone's gold"""

        agents = kwargs.get('aggressiveAgents')

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
            
            amountCollected = self.triggerDigInteraction(agent, goldResource)
            agent.addGold(amountCollected)
            totalAmountCollected += amountCollected
        
        return totalAmountCollected


    def collectiveDigging(self, agents, goldResource):
        """All diggers pool their collections for future distribution."""

        totalAmountCollected = 0

        for agent in agents:

            amountCollected = self.triggerDigInteraction(agent, goldResource)
            totalAmountCollected = totalAmountCollected + amountCollected
        
        return totalAmountCollected

    
    def triggerDigInteraction(self, diggingAgent, goldResource):
        
        return self.actionsHandler.dig(diggingAgent, goldResource)



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