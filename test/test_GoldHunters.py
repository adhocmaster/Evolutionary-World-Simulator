import unittest
from library.GridWorld import GridWorld
from games.GoldHunters.GoldHunters import GoldHunters
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent

class test_GoldHunters(unittest.TestCase):

    def test_MoveAgent(self):
        game = GoldHunters()
        # print(game.world)

        # for id, node in game.world.getNodes().items():
        #     print(node)
        oldLocations = []
        rootLocation = (0, 0)
        for agent in game.agents:
            oldLocation = agent.getLocation()
            if oldLocation[0] != rootLocation[0] or oldLocation[1] != rootLocation[1]:
                oldLocations.append(oldLocation)
            game.moveAgent(agent, rootLocation)

        rootNode = game.world.getNodeAt(rootLocation)

        assert len(game.agents) == len(game.world.getObjectsAtLocation(rootLocation))

        for oldLocation in oldLocations:
            print(oldLocation)
            print(game.world.getObjectsAtLocation(oldLocation))
            print(len(game.world.getObjectsAtLocation(oldLocation)))
            assert 0 == len(game.world.getObjectsAtLocation(oldLocation))




