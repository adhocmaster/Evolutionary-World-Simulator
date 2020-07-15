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
            initialTraits = None, 
            inventory = None, 
            rules = None,
            otherProperties = None
        ):

        super().__init__(id, type)

        self.type = type
        self.id = id
        self.health = health
        self.age =age
        self.populationContribution = populationContribution

        if initialTraits is None:
            self.traits = {} 
        else:
            self.traits = initialTraits
            
        if otherProperties is None:
            self.otherProperties = {} 
        else:
            self.otherProperties = otherProperties



        self.actions = []
        self.offensiveActions = []
        self.defensiveActions = []

        if inventory is None:
            self.inventory = {} 
        else:
            self.inventory = inventory

        if rules is None:
            self.rules = {} 
        else:
            self.rules = rules

        self.history = {}
        
        self.reloadActionsFromTraits()

        pass

    
    def reloadActionsFromTraits(self):
        self.populateActions()
        self.populatePowerActions()


    def populateActions(self):

        self.actions = []
        for traitName in self.traits:
            self.actions.extend(self.traits[traitName].actions)


    def populatePowerActions(self):

        self.offensiveActions = []
        self.defensiveActions = []
        for traitName in self.traits:
            self.offensiveActions.extend( self.traits[traitName].offensiveActions )
            self.defensiveActions.extend( self.traits[traitName].defensiveActions )
        

        pass


    def addToInventory(self, key, value):

        if key in self.inventory:
            self.inventory[key] = self.inventory[key] + value
        else:
            self.updateInventory(key, value)


    def updateInventory(self, key, value):
        self.inventory[key] = value


    def removeFromInventory(self, key, value):

        if key in self.inventory:
            self.inventory[key] -= value
            if self.inventory[key] < 0:
                self.updateInventory(key, 0)
        else:
            self.updateInventory(key, 0)
    

    def getFromInventory(self, key):
        
        if key in self.inventory:
            return self.inventory[key]
        else:
            self.updateInventory(key, 0)
            return 0
            
    
    def deleteKeyFromInventory(self, key):
        self.inventory.pop(self)


    def addTrait(self, trait):
        self.traits[trait.name] = trait
        self.reloadActionsFromTraits()
        pass


    def removeTrait(self, trait):
        self.traits.pop(trait.name)
        self.reloadActionsFromTraits()
        pass


    def removeTraitByName(self, name):
        self.traits.pop(name)
        self.reloadActionsFromTraits()
        pass

    
    def setToOtherProperties(self, key, value):
        self.otherProperties[key] = value
        pass

    
    def getFromOtherProperties(self, key):
        if key in self.otherProperties:
            return self.otherProperties[key]
        else:
            raise Exception(f'No such item in otherProperties with key {key}')
        pass

    
    def takeTurn(self, state):
        pass

