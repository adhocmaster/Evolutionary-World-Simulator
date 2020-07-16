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
        oldLocations = set([])
        rootLocation = (0, 0)
        for agent in game.agents:
            oldLocation = agent.getLocation()
            if oldLocation[0] is not rootLocation[0] or oldLocation[1] is not rootLocation[1]:
                oldLocations.add(oldLocation)
            game.moveAgent(agent, rootLocation)


        assert len(game.agents) == len(game.world.getAgentsAtLocation(rootLocation))

        for oldLocation in oldLocations:
            assert 0 == len(game.world.getAgentsAtLocation(oldLocation))


    def test_RemoveAgentFromOldLocation(self):
        game = GoldHunters()
        oldLocations = set([])
        for agent in game.agents:
            oldLocations.add(agent.getLocation())

        print(oldLocations)

        objectsBefore = 0
        for oldLocation in oldLocations:
            print(game.world.getAgentsAtLocation(oldLocation))
            objectsBefore = objectsBefore + len(game.world.getAgentsAtLocation(oldLocation))

            
        
        for agent in game.agents:
            game.removeAgentFromOldLocation(agent)

        objectsAfter = 0
        for oldLocation in oldLocations:
            print(game.world.getAgentsAtLocation(oldLocation))
            objectsAfter = objectsAfter + len(game.world.getAgentsAtLocation(oldLocation))

        assert objectsBefore == (objectsAfter + len(game.agents))

        

    def testRun(self):
        game = GoldHunters()
        # game.run()


        


