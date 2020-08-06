import unittest
from games.GoldHunters.localLib.GoldHunterEncounter import GoldHunterEncounter
from games.GoldHunters.localLib.GHAgentFactory import GHAgentFactory
from games.GoldHunters.localLib.GoldResource import GoldResource
from library.GridWorld import GridWorld


class test_GoldHunterEncounter(unittest.TestCase):


    def test_getTotalMaxGoldPerTurn(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))
        actualMaxGold = 0

        for digger in diggers:
            actualMaxGold += digger.getMaxGoldPerTurn()

        testMaxGold = encounter.getTotalMaxGoldPerTurn(diggers)

        assert actualMaxGold == testMaxGold

    
    def test_getTotalStrength(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))
        actualTotalStrength = 0

        for digger in diggers:
            actualTotalStrength += digger.getStrength()

        testTotalStrength = encounter.getTotalStrength(diggers)

        assert actualTotalStrength == testTotalStrength


    def test_getAverageStrength(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))
        actualAvgStrength = 0

        for digger in diggers:
            actualAvgStrength += digger.getStrength()
        
        actualAvgStrength /= len(diggers)
        
        testAvgStrength = encounter.getAverageStrength(diggers)

        assert actualAvgStrength == testAvgStrength

        
    def test_getTotalGoldOwned(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))
        actualTotalGold = 90

        for digger in diggers:
            digger.addGold(10)

        testTotalGold = encounter.getTotalGoldOwned(diggers)

        assert actualTotalGold == testTotalGold


    def test_priorityDigging(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()
        
        totalAmountCollected = encounter.priorityDigging(diggers, goldResource)
        
        assert goldResource.getQuantity() == 1000 - totalDiggingPower or goldResource.getQuantity() == 0
        assert totalAmountCollected < totalDiggingPower


        goldResource = GoldResource(1)
        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(100))
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
        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))

        totalDiggingPower = 0
        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        totalAmountCollected = encounter.collectiveDigging(diggers, goldResource)

        assert goldResource.getQuantity() == 1000 - totalDiggingPower


        goldResource = GoldResource(1)
        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))

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

        agents = agentFactory.copyAgents(agentFactory.buildRobbers(9))
        agents[0].strength = 1000000

        strongestAgent = encounterEngine.getStrongestAgent(agents)
        actualStrongestAgent = agents[0]

        assert actualStrongestAgent == strongestAgent

    
    def test_collaboration(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))

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
        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))

        totalDiggingPower = 0

        for digger in diggers:
            totalDiggingPower += digger.getDiggingRate()

        encounter.philanthropy(passiveAgents = diggers, goldResource = goldResource)

        assert goldResource.getQuantity() == 1000 - totalDiggingPower

    
    def test_competition(self):

        agentFactory = GHAgentFactory()
        encounter = GoldHunterEncounter()

        goldResource = GoldResource(1000)
        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))

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
        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(9))

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

        diggers = agentFactory.copyAgents(agentFactory.buildDiggers(4))
        robbers = agentFactory.copyAgents(agentFactory.buildRobbers(4))

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
        originalGoldQuantity = 1000
        goldResource = GoldResource(originalGoldQuantity)

        diggers = agentFactory.buildDiggers(5)
        robbers = agentFactory.buildRobbers(4)


        # single passive encounter
        allEncounterResults = encounter.simulateMultipleEncounters([encounter.collaboration], passiveAgents = diggers, goldResource = goldResource)
        
        for encounterResults in allEncounterResults:
            self.assertIsNotNone(encounterResults.get(goldResource))
            for digger in diggers:
                self.assertIsNotNone(encounterResults.get(digger))
        
        self.assertEqual(originalGoldQuantity, goldResource.getQuantity())


        # all passive encounters
        allEncounterResults = encounter.simulateMultipleEncounters(encounter.passiveEncounters, passiveAgents = diggers, goldResource = goldResource)
        
        for encounterResults in allEncounterResults:
            self.assertIsNotNone(encounterResults.get(goldResource))
            for digger in diggers:
                self.assertIsNotNone(encounterResults.get(digger))
        
        self.assertEqual(originalGoldQuantity, goldResource.getQuantity())


        # single robbing encounter
        allEncounterResults = encounter.simulateMultipleEncounters([encounter.intimidation], passiveAgents = diggers, aggressiveAgents = robbers)
        
        for encounterResults in allEncounterResults:
            for digger in diggers:
                self.assertIsNotNone(encounterResults.get(digger))
            
            for robber in robbers:
                self.assertIsNotNone(encounterResults.get(robber))

            
        # all robbing encounters
        allEncounterResults = encounter.simulateMultipleEncounters(encounter.robbingEncounters, passiveAgents = diggers, aggressiveAgents = robbers)
        
        for encounterResults in allEncounterResults:
            for digger in diggers:
                self.assertIsNotNone(encounterResults.get(digger))
            
            for robber in robbers:
                self.assertIsNotNone(encounterResults.get(robber))


        # single aggressive encounter
        allEncounterResults = encounter.simulateMultipleEncounters([encounter.combat], aggressiveAgents = robbers)
        
        for encounterResults in allEncounterResults:
            for robber in robbers:
                self.assertIsNotNone(encounterResults.get(robber))


        # all aggressive encounters
        allEncounterResults = encounter.simulateMultipleEncounters(encounter.aggressiveEncounters, aggressiveAgents = robbers)
        
        for encounterResults in allEncounterResults:
            for robber in robbers:
                self.assertIsNotNone(encounterResults.get(robber))


        pass

    