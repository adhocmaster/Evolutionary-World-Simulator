from library.AgentFactory import AgentFactory
from GoldHunterAgent import GoldHunterAgent

GHAgentConfig = {

    'diggerEfficiency': 0.8,
    'diggerDiggingRate': 10,
    'diggerStrength': 5,
    'robberEfficiency': 0.2,
    'robberDiggingRate': 5,
    'robberStrength': 10
    
}

class GHAgentFactory(AgentFactory):


    def __init__(self, agentConfig = GHAgentConfig):
        self.agentConfig = agentConfig

    
    def create(self, type, id, efficiency, diggingRate, strength):

        agent = GoldHunterAgent(type = type, id = id)

        agent.setEfficiency(efficiency)
        agent.setDiggingRate(diggingRate)
        agent.setStrength(strength)
        
        return agent


    def buildDigger(self):
        return self.create('digger', 'NA', self.agentConfig['diggerEfficiency'], self.agentConfig['diggerDiggingRate'], self.agentConfig['diggerStrength'])


    def buildRobber(self):
        return self.create('digger', 'NA', self.agentConfig['robberEfficiency'], self.agentConfig['robberDiggingRate'], self.agentConfig['robberStrength'])


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