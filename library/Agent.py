from abc import ABC, abstractmethod
from library.Object import Object

class Agent(Object):

    def __init__(
            self, 
            type, 
            id, 
            health=1, 
            age=0, 
            populationContribution = 1, 
            initialTraits ={}, 
            inventory={}, 
            rules={},
            otherProperties = {}
        ):

        super().__init__(id, type)

        self.type = type
        self.id = id
        self.health = health
        self.age =age
        self.populationContribution = populationContribution
        self.traits = initialTraits
        self.otherProperties = otherProperties

        self.actions = []
        self.offensiveActions = []
        self.defensiveActions = []

        self.inventory = inventory # a dictionary of inventory where keys are resource types and values are amount
        self.rules = rules # keys are types of rules
        self.history = {}
        
        self.reloadTraits()

        pass

    
    def reloadTraits(self):
        self.populateActions()
        self.populatePowerActions()


    def populateActions(self):

        self.actions = []
        for trait in self.traits:
            self.actions.extend(trait.actions)


    def populatePowerActions(self):

        self.offensiveActions = []
        self.defensiveActions = []
        for trait in self.traits:
            self.offensiveActions.extend( trait.offensiveActions )
            self.defensiveActions.extend( trait.defensiveActions )
        

        pass


    def addToInventory(self, key, value):

        if key in self.inventory:
            self.inventory[key] = self.inventory[key] + value
        else:
            self.updateInventory(key, value)

        pass


    def updateInventory(self, key, value):
        self.inventory[key] = value


    def removeFromInventory(self, key):
        self.inventory.pop(self)

    
    def getFromInventory(self, key):
        if key in self.inventory:
            return self.inventory[key]
        else:
            raise Exception(f'No such item in inventory with key {key}')
        pass


    def addTrait(self, trait):
        self.traits[trait.name] = trait
        self.reloadTraits()
        pass


    def removeTrait(self, trait):
        self.traits.pop(trait.name)
        self.reloadTraits()
        pass


    def removeTraitByName(self, name):
        self.traits.pop(name)
        self.reloadTraits()
        pass

    
    def setToOtherProperties(self, key, value):
        self.otherProperties[key] = value
        pass

    
    def getFromOtherProperties(self, key):
        if key in self.otherProperties:
            return self.otherProperties
        else:
            raise Exception(f'No such item in otherProperties with key {key}')
        pass



