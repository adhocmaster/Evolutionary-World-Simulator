from abc import ABC, abstractmethod

class Agent(ABC):

    def __init__(self, type, id, health, age=0, populationContribution = 1, initialTraits ={}, inventory={}, rules={}):
        self.type = type
        self.id = id
        self.health = health
        self.age =age
        self.populationContribution = populationContribution
        self.traits = initialTraits

        self.actions = []
        self.offensiveActions = []
        self.defensiveActions = []

        self.inventory = inventory # a dictionary of inventory where keys are resource types and values are amount
        self.rules = rules # keys are types of rules
        self.history =
        
        self.populateActions()
        self.populatePowerActions()
        pass


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

    