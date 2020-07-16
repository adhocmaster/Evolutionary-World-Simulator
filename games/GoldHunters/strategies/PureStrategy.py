from library.Strategy import Strategy
from games.GoldHunters.localLib.GHAgentType import GHAgentType

class PureStrategy(Strategy):

        
    def changeStrategy(self, agent):

        prevStrategy = None
        if agent.type == GHAgentType.DIGGER:
            agent.type == GHAgentType.ROBBER
            prevStrategy = GHAgentType.DIGGER
        else:
            agent.type == GHAgentType.DIGGER
            prevStrategy = GHAgentType.ROBBER

        agent.updateStrategyProperties()

        agent.logToHistory("Strategy", f"{prevStrategy} -> {agent.type}")

        pass
    

    def getBestAction(self, agent):

        # mix up exploitation and exploration.
        pass
