import unittest
from library.GridWorld import GridWorld
from games.GoldHunters.GoldHunters import GoldHunters
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GHAgentActions import GHAgentActions
from games.GoldHunters.localLib.GoldHunterEncounter import GoldHunterEncounter
from games.GoldHunters.localLib.GHAgentType import GHAgentType


class test_GHAgentActions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.actionsHandler = GHAgentActions()
        cls.agentFactory = GHAgentFactory(actionsHandler=cls.actionsHandler)
        cls.game = GoldHunters(worldSize=(10,10))
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
    

    def checkItemsInPerceivedWorld(self, world, perceivedWorld, bounds):
        # bounds = (left, right, top, bottom)
        for x in range(bounds[0], bounds[1]):
            for y in range(bounds[2], bounds[3]):
                location = (x, y)
                perceivedLocation = (x-bounds[0], y-bounds[2])


                print(world.getAgentsAtLocation(location))
                print(perceivedWorld.getAgentsAtLocation(perceivedLocation))

                assert len(world.getAgentsAtLocation(location)) == len(perceivedWorld.getAgentsAtLocation(perceivedLocation))
                assert len(world.getResourcesAtLocation(location)) == len(perceivedWorld.getResourcesAtLocation(perceivedLocation))

    def test_percieveWorld(self):

        game = test_GHAgentActions.game 
        for agent in game.agents:
            agent.setPerceptionDistance(2)
            game.moveAgent(agent, (5,5))
            agent.actionsHandler.percieveWorld(agent, game.world)
            
            perceivedWorld =  agent.getPerceivedWorld()

            # fail case: world is not 5x5
            assert perceivedWorld.size == (5,5)

            # fail case: world doesn't contain the correct elements
            self.checkItemsInPerceivedWorld(game.world, perceivedWorld, (3, 8, 3, 8))

        # fail case: perceived world out of bounds (agent at corner)
        firstAgent = game.agents[0]
        game.moveAgent(firstAgent, (0,0))

        firstAgent.actionsHandler.percieveWorld(firstAgent, game.world)
        perceivedWorld = firstAgent.getPerceivedWorld()

        assert perceivedWorld.size == (3,3)

        self.checkItemsInPerceivedWorld(game.world, perceivedWorld, (0, 0, 3, 3))


        # fail case: perceived world out of bounds (agent at edge)
        secondAgent = game.agents[1]
        game.moveAgent(secondAgent, (0,5))

        secondAgent.actionsHandler.percieveWorld(secondAgent, game.world)
        perceivedWorld = secondAgent.getPerceivedWorld()

        assert perceivedWorld.size == (3,5)

        self.checkItemsInPerceivedWorld(game.world, perceivedWorld, (0, 3, 3, 8))
