import unittest
from library.GridWorld import GridWorld
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GHAgentActions import GHAgentActions
from games.GoldHunters.localLib.GoldHunterEncounter import GoldHunterEncounter
from games.GoldHunters.localLib.GHAgentType import GHAgentType


class test_GHAgentActions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.actionsHandler = GHAgentActions()
        cls.agentFactory = GHAgentFactory(actionsHandler=cls.actionsHandler)
        pass


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_takeAction(self):

        actionsHandler = test_GHAgentActions.actionsHandler
        agentFactory = test_GHAgentActions.agentFactory
        world = GridWorld()
        agent = agentFactory.buildDigger()
        encounterEngine = GoldHunterEncounter(actionsHandler)

        world.addAgentToLocation((5, 5), agent)
        agent.updateAgentLocation((5, 5))

        actionsHandler.takeAction(agent, world, encounterEngine)
        
        assert agent.getNextAction().name == 'MoveUp'


    def test_updateStrategyProperties(self):

        actionsHandler = test_GHAgentActions.actionsHandler
        agentFactory = test_GHAgentActions.agentFactory
        agent = agentFactory.buildDigger()

        actionsHandler.updateStrategyProperties(agent)

        diggerType = GHAgentType.DIGGER
        assert agent.getEfficiency() == diggerType.value['efficiency']
        assert agent.getDiggingRate() == diggerType.value['diggingRate']
        assert agent.getStrength() == diggerType.value['strength']


    def test_aLocationNearby(self):

        actionsHandler = test_GHAgentActions.actionsHandler
        agentFactory = test_GHAgentActions.agentFactory
        agent = agentFactory.buildDigger()

        agent.updateAgentLocation((0, 0))

        assert actionsHandler.aLocationNearby(agent, (1, 1)) == (1, 1)
        assert actionsHandler.aLocationNearby(agent, (-1, -1)) == (-1, -1)
    

    def test_percieveWorld(self):

        actionsHandler = GHAgentActions()
        agentFactory = GHAgentFactory(actionsHandler=actionsHandler)
        agent = agentFactory.buildDigger()

        world = GridWorld(size=(10, 10))
        world.addAgentToLocation((9, 9), agent)
        agent.updateAgentLocation((9, 9))

        agent.setPerceptionDistance(2)

        actionsHandler.percieveWorld(agent, world)

        print(agent.getPerceivedWorld())
        perceiveWorld =  agent.getPerceivedWorld()

        # fail case: world is not 5x5
        assert perceiveWorld.size == (5,5)

        # TODO list all the fails