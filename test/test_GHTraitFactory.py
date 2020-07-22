import unittest
from games.GoldHunters.localLib.GHTraitFactory import GHTraitFactory
from library.Action import Action
from games.GoldHunters.localLib.GHActionType import GHActionType

class test_TraitFactory(unittest.TestCase):

    def test_createRandom(self):

        factory = GHTraitFactory()

        trait = factory.createRandom()

        # print(trait)
        # print(len(factory.defaultActions))

        print(factory.defaultActions[0])
        # print(GHActionType.MoveUp)
        assert factory.defaultActions[0].name == GHActionType.MoveUp.name
        