import unittest
from library.GridWorld import GridWorld

class test_GridWorld(unittest.TestCase):


    def test_Representation(self):

        world = GridWorld()
        print(world)

    def test_locations(self):
        world = GridWorld(size=(3,3))
        size = world.size

        listOfLocations = []

        for x in range (size[0]):
            for y in range (size[1]):
                listOfLocations.append((x, y))


        assert len(listOfLocations) == len(list(world.locations()))
        