from library.AgentFactory import AgentFactory
from localLib.GoldHungerAgent import GoldHunterAgent

GHAgentConfig = {

    'diggerEfficiency': 0.8,
    'diggerDiggingRate': 10,
    'robberEfficiency': 0.8,
    'robberDiggingRate': 10,


}

class GHAgentFactory(AgentFactory):


    def __init__(self, agentConfig = GHAgentConfig):
        self.agentConfig = agentConfig
        pass

    
    def create(self, type, id, efficiency, diggingRate):
        agent = GoldHunterAgent(type = type, id = id)
        agent.setToOtherProperties('efficiency', efficiency)
        agent.setToOtherProperties('diggingRate', diggingRate)
        return agent

    
    def buildDigger(self):
        return self.create('digger', 'NA', self.agentConfig['diggerEfficiency'], self.agentConfig['diggerDiggingRate'])


    def buildRobber(self):
        return self.create('digger', 'NA', self.agentConfig['robberEfficiency'], self.agentConfig['robberDiggingRate'])


    def buildDiggers(self, numberOfDiggers = 10):
        # TODO
        pass