import unittest
from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GHAgentActions import GHAgentActions

class test_GoldHunterAgent(unittest.TestCase):

    def test_init(self):
        agentFactory = GHAgentFactory(actionsHandler = GHAgentActions())
        agent = agentFactory.buildDigger()
