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
            GHMoveAction(GHActionType.MoveUp), 
            GHMoveAction(GHActionType.MoveDown), 
            GHMoveAction(GHActionType.MoveLeft), 
            GHMoveAction(GHActionType.MoveRight), 
            GHMoveAction(GHActionType.MoveUpLeft),
            GHMoveAction(GHActionType.MoveUpRight), 
            GHMoveAction(GHActionType.MoveDownLeft), 
            GHMoveAction(GHActionType.MoveDownRight),
            Action(GHActionType.Dig.name),
            Action(GHActionType.Rob.name)
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
