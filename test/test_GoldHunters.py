import unittest
from library.GridWorld import GridWorld
from games.GoldHunters.GoldHunters import GoldHunters
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent

class test_GoldHunters(unittest.TestCase):

    def test_MoveAgent(self):
        game = GoldHunters()
        print(game.world)

