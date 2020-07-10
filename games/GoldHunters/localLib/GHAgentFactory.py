from library.AgentFactory import AgentFactory
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent
from games.GoldHunters.localLib.GHTraitFactory import GHTraitFactory
import uuid
import random

GHAgentConfig = {

    'diggerEfficiency': 0.8,
    'diggerDiggingRate': 10,
    'diggerStrength': 5,
    'robberEfficiency': 0.2,
    'robberDiggingRate': 5,
    'robberStrength': 10,
    'minPerceptionDistance': 1,
    'maxPerceptionDistance': 3
    
}

class GHAgentFactory(AgentFactory):


    def __init__(self, agentConfig = GHAgentConfig):
        self.agentConfig = agentConfig
        self.traitFactory = GHTraitFactory()

    
    def create(self, type, id, efficiency, diggingRate, strength, perceptionDistance):

        agent = GoldHunterAgent(type = type, id = id)

        agent.setEfficiency(efficiency)
        agent.setDiggingRate(diggingRate)
        agent.setStrength(strength)
        agent.setPerceptionDistance(perceptionDistance)
        
        return agent


    def buildDigger(self):
        self.traitFactory.createRandom()
        
        id = hex(uuid.getnode())
        perceptionDistance = random.randint(self.agentConfig['minPerceptionDistance'], self.agentConfig['maxPerceptionDistance'])
        return self.create('digger', id, self.agentConfig['diggerEfficiency'], self.agentConfig['diggerDiggingRate'], self.agentConfig['diggerStrength'], perceptionDistance)


    def buildRobber(self):
        self.traitFactory.createRandom()

        id = hex(uuid.getnode())
        perceptionDistance = random.randint(self.agentConfig['minPerceptionDistance'], self.agentConfig['maxPerceptionDistance'])
        return self.create('robber', id, self.agentConfig['robberEfficiency'], self.agentConfig['robberDiggingRate'], self.agentConfig['robberStrength'], perceptionDistance)


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