from abc import ABC, abstractmethod

class Agent(ABC):

    def __init__(self, type, id, health, initialTraits):
        self.type = type
        self.id = id
        self.health = health
        self.traits = initialTraits

        self.actions = []
        self.offensiveActions = []
        self.defensiveActions = []
        
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

