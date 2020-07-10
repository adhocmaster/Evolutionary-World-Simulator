import unittest
from library.TraitFactory import TraitFactory
from library.Action import Action

class test_TraitFactory(unittest.TestCase):

    def test_createRandom(self):

        factory = TraitFactory()

        trait = factory.createRandom()

        print(trait)

        assert factory.defaultActions[0].name == 'MoveUp'