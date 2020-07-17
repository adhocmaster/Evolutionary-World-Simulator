import unittest
from games.GoldHunters.localLib.GoldHunterEncounter import GoldHunterEncounter
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GoldResource import GoldResource

class test_GoldHunterEncounter(unittest.TestCase):


    def test_getTotalMaxGoldPerTurn(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = agentFactory.buildDiggers()
        actualMaxGold = 0

        for digger in diggers:
            actualMaxGold += digger.getMaxGoldPerTurn()

        testMaxGold = encounter.getTotalMaxGoldPerTurn(diggers)

        assert actualMaxGold == testMaxGold

    
    def test_getTotalStrength(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = agentFactory.buildDiggers()
        actualTotalStrength = 0

        for digger in diggers:
            actualTotalStrength += digger.getStrength()

        testTotalStrength = encounter.getTotalStrength(diggers)

        assert actualTotalStrength == testTotalStrength


    def test_getAverageStrength(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = agentFactory.buildDiggers()
        actualAvgStrength = 0

        for digger in diggers:
            actualAvgStrength += digger.getStrength()
        
        actualAvgStrength /= len(diggers)
        
        testAvgStrength = encounter.getAverageStrength(diggers)

        assert actualAvgStrength == testAvgStrength

        
    def test_getTotalGoldOwned(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = agentFactory.buildDiggers(10)
        actualTotalGold = 100

        for digger in diggers:
            digger.addGold(10)

        testTotalGold = encounter.getTotalGoldOwned(diggers)

        assert actualTotalGold == testTotalGold


    def test_priorityDigging(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = agentFactory.buildDiggers(10)

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()
        
        totalAmountCollected = encounter.priorityDigging(diggers, goldResource)
        
        assert goldResource.getQuantity() == 1000 - totalDiggingPower or goldResource.getQuantity() == 0
        assert totalAmountCollected < totalDiggingPower


        goldResource = GoldResource(1)
        diggers = agentFactory.buildDiggers(100)
        lastAgent = diggers[len(diggers) - 1]
        originalLastAgentGold = lastAgent.getGold()

        encounter.priorityDigging(diggers, goldResource)

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        assert goldResource.getQuantity() == 0
        assert lastAgent.getGold() == originalLastAgentGold


    def test_collectiveDigging(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = agentFactory.buildDiggers(10)

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        totalAmountCollected = encounter.collectiveDigging(diggers, goldResource)

        assert goldResource.getQuantity() == 1000 - totalDiggingPower


        goldResource = GoldResource(1)
        diggers = agentFactory.buildDiggers(100)

        encounter.priorityDigging(diggers, goldResource)

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        assert goldResource.getQuantity() == 0

    
    def test_collaboration(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = agentFactory.buildDiggers(10)

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        encounter.collaboration(passiveAgents = diggers, goldResource = goldResource)

        assert goldResource.getQuantity() == 1000 - totalDiggingPower

    
    def test_getAllEncounters(self):

        encounterEngine = GoldHunterEncounter()

        encounters = encounterEngine.getAllEncounters()

        actualEncounters = encounterEngine.passiveEncounters + encounterEngine.robbingEncounters + encounterEngine.aggressiveEncounters

        assert encounters == actualEncounters

    
    def test_addTuples(self):

        encounterEngine = GoldHunterEncounter()

        tuple1 = (5, 7)
        tuple2 = (8, 1)

        addedTuple = encounterEngine.addTuples(tuple1, tuple2)
        actualAddedTuple = (13, 8)

        assert addedTuple == actualAddedTuple

    
    def test_getStrongestAgent(self):

        agentFactory = GHAgentFactory()
        encounterEngine = GoldHunterEncounter()

        agents = agentFactory.buildRobbers(10)
        agents[0].setStrength(1000000)

        strongestAgent = encounterEngine.getStrongestAgent(agents)
        actualStrongestAgent = agents[0]

        assert actualStrongestAgent == strongestAgent

    
    