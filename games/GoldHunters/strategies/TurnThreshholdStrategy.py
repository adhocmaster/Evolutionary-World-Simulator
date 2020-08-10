from games.GoldHunters.strategies.PureStrategy import PureStrategy

"""
strategies are stateless objects. Never add states to them as they are used as singletons.
"""
class TurnThreshholdStrategy(PureStrategy):

    def needChange(self, agent):

        # TODO decide whether the agent needs to change.

        if len(agent.previousGoldOwned) == agent.productionHistoryLength:

            goldGained = agent.previousGoldOwned[4] - agent.previousGoldOwned[0]

            if goldGained < agent.goldQuota:
                return True

        return False


    
    def changeStrategy(self, agent):
        super().changeStrategy(agent) # We are currently using only pure strategies.
        pass


    def getBestAction(self, agent):

        # mix up exploitation and exploration.
        pass
