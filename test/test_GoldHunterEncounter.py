import unittest
from games.GoldHunters.localLib.GoldHunterEncounter import GoldHunterEncounter
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GoldResource import GoldResource
from games.GoldHunters.localLib.GHSimulatedAgent import GHSimulatedAgent


class test_GoldHunterEncounter(unittest.TestCase):


    def test_getTotalMaxGoldPerTurn(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers()]
        actualMaxGold = 0

        for digger in diggers:
            actualMaxGold += digger.getMaxGoldPerTurn()

        testMaxGold = encounter.getTotalMaxGoldPerTurn(diggers)

        assert actualMaxGold == testMaxGold

    
    def test_getTotalStrength(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers()]
        actualTotalStrength = 0

        for digger in diggers:
            actualTotalStrength += digger.getStrength()

        testTotalStrength = encounter.getTotalStrength(diggers)

        assert actualTotalStrength == testTotalStrength


    def test_getAverageStrength(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers()]
        actualAvgStrength = 0

        for digger in diggers:
            actualAvgStrength += digger.getStrength()
        
        actualAvgStrength /= len(diggers)
        
        testAvgStrength = encounter.getAverageStrength(diggers)

        assert actualAvgStrength == testAvgStrength

        
    def test_getTotalGoldOwned(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers(10)]
        actualTotalGold = 100

        for digger in diggers:
            digger.addGold(10)

        testTotalGold = encounter.getTotalGoldOwned(diggers)

        assert actualTotalGold == testTotalGold


    def test_priorityDigging(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers(10)]

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()
        
        totalAmountCollected = encounter.priorityDigging(diggers, goldResource)
        
        assert goldResource.getQuantity() == 1000 - totalDiggingPower or goldResource.getQuantity() == 0
        assert totalAmountCollected < totalDiggingPower


        goldResource = GoldResource(1)
        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers(100)]
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
        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers(10)]

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        totalAmountCollected = encounter.collectiveDigging(diggers, goldResource)

        assert goldResource.getQuantity() == 1000 - totalDiggingPower


        goldResource = GoldResource(1)
        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers(100)]

        encounter.priorityDigging(diggers, goldResource)

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        assert goldResource.getQuantity() == 0

    
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

        agents = [GHSimulatedAgent(r) for r in agentFactory.buildRobbers(10)]
        agents[0].strength = 1000000

        strongestAgent = encounterEngine.getStrongestAgent(agents)
        actualStrongestAgent = agents[0]

        assert actualStrongestAgent == strongestAgent

    
    def test_collaboration(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = [d for d in agentFactory.buildDiggers(9)]

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        encounter.collaboration(passiveAgents = diggers, goldResource = goldResource)

        print(f"current in resource: {goldResource.getQuantity()}")
        print(f"total lost: {totalDiggingPower}")

        assert goldResource.getQuantity() == 1000 - totalDiggingPower


    def test_philanthropy(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers(9)]

        totalDiggingPower = 0

        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        encounter.philanthropy(passiveAgents = diggers, goldResource = goldResource)

        assert goldResource.getQuantity() == 1000 - totalDiggingPower

    
    def test_competition(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers(9)]

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        encounter.competition(passiveAgents = diggers, goldResource = goldResource)

        assert goldResource.getQuantity() == 1000 - totalDiggingPower
        

        goldResource = GoldResource(100)

        oldGoldValues = {}
        for digger in diggers:
            oldGoldValues[digger] = digger.getGold()

        encounter.competition(passiveAgents = diggers, goldResource = goldResource)

        for digger in oldGoldValues.keys():
            oldGoldValue = oldGoldValues[digger]
            assert digger.getGold() - oldGoldValue <= digger.getMaxGoldPerTurn()

    
    def test_monopoly(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers(9)]

        totalDiggingPower = 0

        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        encounter.monopoly(passiveAgents = diggers, goldResource = goldResource)

        assert goldResource.getQuantity() == 1000 - totalDiggingPower


        goldResource = GoldResource(1)

        for digger in diggers:
            digger.setGold(0)

        diggers[0].strength = 10000000

        encounter.monopoly(passiveAgents = diggers, goldResource = goldResource)

        self.assertEqual(1, diggers[0].getGold())

    
    def test_intimidation(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = [GHSimulatedAgent(d) for d in agentFactory.buildDiggers(4)]
        robbers = [GHSimulatedAgent(r) for r in agentFactory.buildRobbers(4)]

        totalDiggerStrength = encounter.getTotalStrength(diggers)
        totalRobberStrength = encounter.getTotalStrength(robbers)

        oldRobberGold = {}
        for robber in robbers:
            robber.addGold(100)
            oldRobberGold[robber] = robber.getGold()

        oldDiggerGold = {}
        for digger in diggers:
            digger.addGold(100)
            oldDiggerGold[digger] = digger.getGold()

        encounter.intimidation(aggressiveAgents = robbers, passiveAgents = diggers)

        if totalRobberStrength >= 2 * totalDiggerStrength:
            pass
        # TODO continue making the test

        pass


    def test_simulateMultipleEncounters(self):
        # TODO continue
        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        

        pass

    