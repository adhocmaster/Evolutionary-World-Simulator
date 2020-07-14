from library.TraitFactory import TraitFactory
from library.Trait import Trait
from library.ActionFactory import ActionFactory
# from library.Action import Action
from games.GoldHunters.localLib.GHMoveAction import GHMoveAction
import random

class GHTraitFactory(TraitFactory):

    def __init__(self):
        self.randomTraitLastId = 0

        self.defaultActions = [
            GHMoveAction('MoveUp', (0, 1)), 
            GHMoveAction('MoveDown', (0, -1)), 
            GHMoveAction('MoveLeft', (-1, 0)), 
            GHMoveAction('MoveRight', (1, 0)), 
            GHMoveAction('MoveUpLeft', (-1, 1)),
            GHMoveAction('MoveUpRight', (1, 1)), 
            GHMoveAction('MoveDownLeft', (-1, -1)), 
            GHMoveAction('MoveDownRight', (1, -1))
        ]

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
