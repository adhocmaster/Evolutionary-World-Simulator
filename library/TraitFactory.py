
from library.Action import Action
from library.Trait import Trait
from library.ActionFactory import ActionFactory
import random

class TraitFactory:

    def __init__(self):

        self.randomTraitLastId = 0

        self.defaultActions = [Action('MoveUp'), Action('MoveDown'), Action('MoveLeft'), Action('MoveRight')]

        pass

    def create(self, name, actions, offensiveActions, defensiveActions):
        return Trait(name, actions, offensiveActions, defensiveActions)

    

    def createRandom(self):

        self.randomTraitLastId += 1
        name = 'trait-' + str(self.randomTraitLastId)

        actions = self.defaultActions

        actionFactory = ActionFactory()

        numberOfPowers = random.randint(1, 5)
        offensiveActions = []
        defensiveActions = []

        for _ in range(numberOfPowers):
            power = actionFactory.createRandomPower()
            if power.powerType.name.find('_DEF') != -1:
                offensiveActions.append(power)
            else:
                defensiveActions.append(power)

        return Trait(name, actions, offensiveActions, defensiveActions)

        
