from games.GoldHunters.localLib.GoldHunterAgent import GoldHunterAgent


class GHSimulatedAgent:

    def __init__(self, originalAgent: GoldHunterAgent):

        self.diggingRate = originalAgent.getDiggingRate()
        self.efficiency = originalAgent.getEfficiency()
        self.strength = originalAgent.getStrength()

        self.gold = originalAgent.getGold()


    def getMaxGoldPerTurn(self):
        return self.getDiggingRate() * self.getEfficiency()


    def getDiggingRate(self):
        return self.diggingRate

    
    def getEfficiency(self):
        return self.efficiency

    
    def getStrength(self):
        return self.strength

    
    def getGold(self):
        return self.gold

    
    def addGold(self, amountToAdd):
        self.gold += amountToAdd

    
    def removeGold(self, amountToRemove):
        self.gold -= amountToRemove
        
        if self.gold < 0:
            self.gold = 0

        pass

    
    def setGold(self, newGoldAmount):
        self.gold = newGoldAmount