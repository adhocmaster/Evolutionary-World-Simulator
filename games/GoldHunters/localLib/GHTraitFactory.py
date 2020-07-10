from library.TraitFactory import TraitFactory
from library.Trait import Trait
from library.ActionFactory import ActionFactory
from library.Action import Action
import random

class GHTraitFactory(TraitFactory):

    def __init__(self):
        self.randomTraitLastId = 0

        self.defaultActions = [Action('MoveUp'), Action('MoveDown'), Action('MoveLeft'), Action('MoveRight'), Action('MoveUpLeft') , Action('MoveUpRight'), Action('MoveDownLeft'), Action('MoveDownRight')]

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
