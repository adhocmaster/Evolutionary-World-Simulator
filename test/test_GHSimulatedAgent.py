import unittest
from games.GoldHunters.localLib.GHSimulatedAgent import GHSimulatedAgent
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GHAgentActions import GHAgentActions


class test_GHSimulatedAgent(unittest.TestCase):
    
    def test_init(self):
        agentFactory = GHAgentFactory(GHAgentActions())
        originalAgent = agentFactory.buildDigger()

        simAgent = GHSimulatedAgent(originalAgent)

        self.assertNotEqual(originalAgent, simAgent)

        self.assertEqual(originalAgent.getGold(), simAgent.gold)
        self.assertEqual(originalAgent.getDiggingRate(), simAgent.diggingRate)
        self.assertEqual(originalAgent.getEfficiency(), simAgent.efficiency)
        self.assertEqual(originalAgent.getStrength(), simAgent.strength)
    

    def test_simpleGetters(self):
        agentFactory = GHAgentFactory()
        originalAgent = agentFactory.buildDigger()

        simAgent = GHSimulatedAgent(originalAgent)

        self.assertEqual(originalAgent.getGold(), simAgent.getGold())
        self.assertEqual(originalAgent.getDiggingRate(), simAgent.getDiggingRate())
        self.assertEqual(originalAgent.getEfficiency(), simAgent.getEfficiency())
        self.assertEqual(originalAgent.getStrength(), simAgent.getStrength())

        simAgent.strength = -5
        self.assertNotEqual(originalAgent.getStrength(), simAgent.getStrength())

    
    def test_getMaxGoldPerTurn(self):
        agentFactory = GHAgentFactory()
        originalAgent = agentFactory.buildDigger()

        simAgent = GHSimulatedAgent(originalAgent)

        self.assertEqual(originalAgent.getMaxGoldPerTurn(), simAgent.getMaxGoldPerTurn())

    
    def test_changeGoldValue(self):
        agentFactory = GHAgentFactory()
        originalAgent = agentFactory.buildDigger()

        simAgent = GHSimulatedAgent(originalAgent)

        simAgent.setGold(0)
        self.assertEqual(0, simAgent.getGold())

        simAgent.addGold(30)
        self.assertEqual(30, simAgent.getGold())

        simAgent.removeGold(20)
        self.assertEqual(10, simAgent.getGold())

        simAgent.removeGold(20)
        self.assertEqual(0, simAgent.getGold())

        
    pass