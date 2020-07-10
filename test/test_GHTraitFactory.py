import unittest
from games.GoldHunters.localLib.GHTraitFactory import GHTraitFactory
from library.Action import Action

class test_TraitFactory(unittest.TestCase):

    def test_createRandom(self):

        factory = GHTraitFactory()

        trait = factory.createRandom()

        print(trait)
        print(len(factory.defaultActions))

        assert factory.defaultActions[0].name == 'MoveUp'
        assert factory.defaultActions[7].name == 'MoveDownRight'