from library.AgentFactory import AgentFactory
<<<<<<< HEAD
from GoldHunterAgent import GoldHunterAgent
=======
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent
>>>>>>> 6ae9b57c18ef5ec39a1bbbad7edd77f33d9bc6cc

GHAgentConfig = {

    'diggerEfficiency': 0.8,
    'diggerDiggingRate': 10,
<<<<<<< HEAD
    'diggerStrength': 5,
    'robberEfficiency': 0.4,
    'robberDiggingRate': 5,
    'robberStrength': 10

=======
    'robberEfficiency': 0.2,
    'robberDiggingRate': 5,
>>>>>>> 6ae9b57c18ef5ec39a1bbbad7edd77f33d9bc6cc

}

class GHAgentFactory(AgentFactory):


    def __init__(self, agentConfig = GHAgentConfig):
        self.agentConfig = agentConfig
        pass

    
    def create(self, type, id, efficiency, diggingRate, strength):
        agent = GoldHunterAgent(type = type, id = id)
<<<<<<< HEAD
        agent.setToOtherProperties('efficiency', efficiency)
        agent.setToOtherProperties('diggingRate', diggingRate)
        agent.setToOtherProperties('strength', strength)
=======
        agent.setToOtherProperties('efficiency', efficiency) # TODO replace with GoldHunterAgent method
        agent.setToOtherProperties('diggingRate', diggingRate) # TODO replace with GoldHunterAgent method
>>>>>>> 6ae9b57c18ef5ec39a1bbbad7edd77f33d9bc6cc
        return agent

    
    def buildDigger(self):
        return self.create('digger', 'NA', self.agentConfig['diggerEfficiency'], self.agentConfig['diggerDiggingRate'], self.agentConfig['diggerStrength'])


    def buildRobber(self):
        return self.create('digger', 'NA', self.agentConfig['robberEfficiency'], self.agentConfig['robberDiggingRate'], self.agentConfig['robberStrength'])


    def buildDiggers(self, numberOfDiggers = 10):
        # TODO
        pass