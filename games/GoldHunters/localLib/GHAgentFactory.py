from library.AgentFactory import AgentFactory
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent
from games.GoldHunters.localLib.GHTraitFactory import GHTraitFactory
from games.GoldHunters.localLib.GHAgentType import GHAgentType
from games.GoldHunters.strategies.TurnThreshholdStrategy import TurnThreshholdStrategy
from games.GoldHunters.localLib.GHAgentActions import GHAgentActions
import uuid
import random

GHAgentConfig = {

    'minPerceptionDistance': 1,
    'maxPerceptionDistance': 3
    
}

class GHAgentFactory(AgentFactory):


    def __init__(self, actionsHandler = None, agentConfig = GHAgentConfig, strategy = None):

        self.defaultLocation = (-1, -1)
        self.agentConfig = agentConfig
        self.traitFactory = GHTraitFactory()
        self.strategy = strategy
        self.defaultStrategy = TurnThreshholdStrategy()
        

        if actionsHandler is None:
            print("Warning: creating the default actionsHandler")
            # raise Exception("GHAgentFactory needs an actionsHandler.")
            self.actionsHandler = GHAgentActions()
        else:
            self.actionsHandler = actionsHandler
        pass

    
    def create(self, type, id, trait, perceptionDistance):

        agent = GoldHunterAgent(type = type, id = id, productionHistoryLength = 5, goldQuota = 1, actionsHandler = self.actionsHandler)

        agent.setEfficiency(type.value['efficiency'])
        agent.setDiggingRate(type.value['diggingRate'])
        agent.setStrength(type.value['strength'])
        agent.setPerceptionDistance(perceptionDistance)
        agent.updateAgentLocation(self.defaultLocation)
        
        agent.addTrait(trait)

        if self.strategy is None:
            agent.strategy = self.defaultStrategy
        else:
            agent.strategy = self.strategy
       
        return agent


    def buildDigger(self):
        trait = self.traitFactory.createRandom()
        
        id = hex(uuid.getnode())
        perceptionDistance = random.randint(self.agentConfig['minPerceptionDistance'], self.agentConfig['maxPerceptionDistance'])
        return self.create(GHAgentType.DIGGER, id, trait, perceptionDistance)


    def buildRobber(self):
        trait = self.traitFactory.createRandom()

        id = hex(uuid.getnode())
        perceptionDistance = random.randint(self.agentConfig['minPerceptionDistance'], self.agentConfig['maxPerceptionDistance'])
        return self.create(GHAgentType.ROBBER, id, trait, perceptionDistance)


    def buildDiggers(self, numberOfDiggers = 10):

        diggersMade = []

        for _ in range(numberOfDiggers):
            diggersMade.append(self.buildDigger())

        return diggersMade


    def buildRobbers(self, numberOfRobbers = 10):

        robbersMade = []

        for _ in range(numberOfRobbers):
            robbersMade.append(self.buildRobber())

        return robbersMade


    def copyAgents(self, agents):

        copies = []

        for agent in agents:
            copies.append(self.copyAgent(agent))

        return copies
        

    def copyAgent(self, agent):

        newAgent = GoldHunterAgent(agent.type, 
                                    None, 
                                    productionHistoryLength = agent.productionHistoryLength, 
                                    goldQuota= agent.goldQuota, 
                                    actionsHandler= agent.actionsHandler)

        newAgent.setDiggingRate(agent.getDiggingRate())
        newAgent.setEfficiency(agent.getEfficiency())
        newAgent.setStrength(agent.getStrength())

        newAgent.setGold(agent.getGold())

        return newAgent