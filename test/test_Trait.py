import unittest
from library.TraitFactory import TraitFactory

class test_TraitFactory(unittest.TestCase):

    def test_createRandom(self):

        factory = TraitFactory()

        trait = factory.createRandom()

        print(trait)