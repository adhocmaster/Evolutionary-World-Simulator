import unittest
from library.GridWorld import GridWorld

class test_GridWorld(unittest.TestCase):


    def test_Representation(self):

        world = GridWorld()
        print(world)