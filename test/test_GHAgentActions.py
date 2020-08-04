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
        world = GridWorld(size = (10, 10))
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

        gridWorld = GridWorld(size=(10, 10))

        # testing agent on the world border
        agent.updateAgentLocation((0, 0))
        self.assertEqual(actionsHandler.aLocationNearby(agent, (1, 1), gridWorld), (1, 1))
        self.assertEqual(actionsHandler.aLocationNearby(agent, (1, 0), gridWorld), (1, 0))
        self.assertEqual(actionsHandler.aLocationNearby(agent, (0, 1), gridWorld), (0, 1))
        with self.assertRaises(Exception):
            actionsHandler.aLocationNearby(agent, (0, -1), gridWorld)

        # testing agent in the middle
        agent.updateAgentLocation((5, 5))
        self.assertEqual(actionsHandler.aLocationNearby(agent, (1, 1), gridWorld), (6, 6))
        self.assertEqual(actionsHandler.aLocationNearby(agent, (1, 0), gridWorld), (6, 5))
        self.assertEqual(actionsHandler.aLocationNearby(agent, (0, 1), gridWorld), (5, 6))
        self.assertEqual(actionsHandler.aLocationNearby(agent, (0, -1), gridWorld), (5, 4))


    def test_perceiveWorld(self):

        game = test_GHAgentActions.game 
        for agent in game.agents:
            agent.setPerceptionDistance(2)
            game.moveAgent(agent, (5,5))
            agent.actionsHandler.perceiveWorld(agent, game.world)

            perceivedWorld =  agent.getPerceivedWorld()

            # fail case: world is not 5x5
            assert perceivedWorld.size == (5,5)

            # fail case: world doesn't contain the correct elements
            self.checkItemsInPerceivedWorld(game.world, perceivedWorld, (3, 8, 3, 8))

        # fail case: perceived world out of bounds (agent at corner)
        firstAgent = game.agents[0]
        game.moveAgent(firstAgent, (0,0))

        firstAgent.actionsHandler.perceiveWorld(firstAgent, game.world)
        perceivedWorld = firstAgent.getPerceivedWorld()

        assert perceivedWorld.size == (3,3)

        self.checkItemsInPerceivedWorld(game.world, perceivedWorld, (0, 0, 3, 3))


        # fail case: perceived world out of bounds (agent at edge)
        secondAgent = game.agents[1]
        game.moveAgent(secondAgent, (0,5))

        secondAgent.actionsHandler.perceiveWorld(secondAgent, game.world)
        perceivedWorld = secondAgent.getPerceivedWorld()

        assert perceivedWorld.size == (3,5)

        self.checkItemsInPerceivedWorld(game.world, perceivedWorld, (0, 3, 3, 8))


    def checkItemsInPerceivedWorld(self, world, perceivedWorld, bounds):
        # bounds = (left, right, top, bottom) 
        # right and bottom is not included.
        for x in range(bounds[0], bounds[1]):
            for y in range(bounds[2], bounds[3]):
                location = (x, y)
                perceivedLocation = (x-bounds[0], y-bounds[2])


                print(world.getAgentsAtLocation(location))
                print(perceivedWorld.getAgentsAtLocation(perceivedLocation))

                assert len(world.getAgentsAtLocation(location)) == len(perceivedWorld.getAgentsAtLocation(perceivedLocation))
                assert len(world.getResourcesAtLocation(location)) == len(perceivedWorld.getResourcesAtLocation(perceivedLocation))


    def test_dig(self):
        game = test_GHAgentActions.game
        actionsHandler = test_GHAgentActions.actionsHandler
        agent = game.agents[0]
        resource = game.resources[0]
        oldResourceQuantity = resource.quantity

        actionsHandler.dig(agent, resource)

        self.assertGreaterEqual(oldResourceQuantity, resource.quantity)


    def test_getMaxCollectableFromResource(self):
        game = test_GHAgentActions.game
        actionsHandler = test_GHAgentActions.actionsHandler
        goldResource = game.resources[0]
        goldResource.setQuantity(100)
        agent = game.agents[0]

        collectableAmount = actionsHandler.getMaxCollectableFromResource(agent, goldResource) 
        self.assertLess(collectableAmount, goldResource.amountPerDig(agent.getDiggingRate()))
 

    def test_getMaxCollectableFromResources(self):
        game = test_GHAgentActions.game
        actionsHandler = test_GHAgentActions.actionsHandler
        resources = game.resources
        agent = game.agents[0]

        actionsHandler.getMaxCollectableFromResources(agent, resources)


    def test_calculateBounds(self):
        actionsHandler = test_GHAgentActions.actionsHandler
        world = GridWorld()

        perceptonDistance = 2
        location = (5,5)

        bounds = actionsHandler.calculateBounds(location, world, perceptonDistance)

        assert bounds[0] == 3
        assert bounds[1] == 8
        assert bounds[2] == 3
        assert bounds[3] == 8

        ## add boundary cases where bounds is determined by gridWorld size instead of perception distance


    

