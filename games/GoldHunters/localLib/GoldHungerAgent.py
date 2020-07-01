from library.Agent import Agent

class GoldHunterAgent(Agent):

    # needed properties:
    # 1. efficiency : .8 means it can get a maximum of 80% of the gold
    # 2. diggingRate: x amount per turn from a resource
    # 3. max amount of gold per turn: efficiency * diggingRate.

    def addGold(self, amount):
        self.addToInventory('gold', amount)
        pass

    
    def getEfficiency(self):
        pass
    

    def getDiggingRate(self):
        pass

    