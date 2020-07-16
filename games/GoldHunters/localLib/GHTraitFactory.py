from library.TraitFactory import TraitFactory
from library.Trait import Trait
from library.Action import Action
from games.GoldHunters.localLib.GHActionType import GHActionType
from library.ActionFactory import ActionFactory
# from library.Action import Action
from games.GoldHunters.localLib.GHMoveAction import GHMoveAction
import random

class GHTraitFactory(TraitFactory):

    def __init__(self):
        self.randomTraitLastId = 0

        self.defaultActions = [
            GHMoveAction(GHActionType.MoveUp, (0, 1)), 
            GHMoveAction(GHActionType.MoveDown, (0, -1)), 
            GHMoveAction(GHActionType.MoveLeft, (-1, 0)), 
            GHMoveAction(GHActionType.MoveRight, (1, 0)), 
            GHMoveAction(GHActionType.MoveUpLeft, (-1, 1)),
            GHMoveAction(GHActionType.MoveUpRight, (1, 1)), 
            GHMoveAction(GHActionType.MoveDownLeft, (-1, -1)), 
            GHMoveAction(GHActionType.MoveDownRight, (1, -1)),
            Action(GHActionType.Dig),
            Action(GHActionType.Rob)
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
