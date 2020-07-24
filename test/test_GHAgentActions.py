import unittest
from library.GridWorld import GridWorld
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GHAgentActions import GHAgentActions
from games.GoldHunters.localLib.GoldHunterEncounter import GoldHunterEncounter
from games.GoldHunters.localLib.GHAgentType import GHAgentType


class test_GHAgentActions(unittest.TestCase):

    def test_takeAction(self):

        actionsHandler = GHAgentActions()
        agentFactory = GHAgentFactory(actionsHandler=actionsHandler)
        world = GridWorld()
        agent = agentFactory.buildDigger()
        encounterEngine = GoldHunterEncounter(actionsHandler)

        world.addAgentToLocation((5, 5), agent)
        agent.updateAgentLocation((5, 5))

        actionsHandler.takeAction(agent, world, encounterEngine)
        
        assert agent.getNextAction().name == 'MoveUp'


    def test_updateStrategyProperties(self):

        actionsHandler = GHAgentActions()
        agentFactory = GHAgentFactory(actionsHandler=actionsHandler)
        agent = agentFactory.buildDigger()

        actionsHandler.updateStrategyProperties(agent)

        diggerType = GHAgentType.DIGGER
        assert agent.getEfficiency() == diggerType.value['efficiency']
        assert agent.getDiggingRate() == diggerType.value['diggingRate']
        assert agent.getStrength() == diggerType.value['strength']

    def test_aLocationNearby(self):

        actionsHandler = GHAgentActions()
        agentFactory = GHAgentFactory(actionsHandler=actionsHandler)
        agent = agentFactory.buildDigger()

        agent.updateAgentLocation((0, 0))

        assert actionsHandler.aLocationNearby(agent, (1, 1)) == (1, 1)
        assert actionsHandler.aLocationNearby(agent, (-1, -1)) == (-1, -1)
