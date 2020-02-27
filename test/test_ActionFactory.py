import unittest
from library.ActionFactory import ActionFactory

class test_ActionFactory(unittest.TestCase):


    def test_NewAction(self):
        factory = ActionFactory()
        action = factory.create("MoveRight")

        assert action.name == "MoveRight"
        assert action.power == 0
        assert action.powerType is None

