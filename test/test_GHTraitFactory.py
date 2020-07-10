import unittest
from games.GoldHunters.localLib.GHTraitFactory import GHTraitFactory
from library.Action import Action

class test_TraitFactory(unittest.TestCase):

    def test_createRandom(self):

        factory = GHTraitFactory()

        trait = factory.createRandom()

        print(trait)

        assert factory.defaultActions[0] == Action('MoveUp')
        assert factory.defaultActions[8] == Action('MoveDownRight')