from library.PowerType import PowerType
from library.Action import Action
import numpy as np
import random

class ActionFactory:

    """This helps to create common actions and keep them consistent. Not thread-safe"""
    def __init__(self):

        self.actions = {} # name: powerType 
        self.randomActionLastId = 0

        pass

    def createPower(self, name, powerType:PowerType, power = 10):

        if name in self.actions:
            existingPowerType = self.actions[name]
            if existingPowerType != powerType:
                raise Exception(f"There exists an action {name} which has a different powerType, {existingPowerType} than the new one {powerType}")
            else:
                self.actions[name] = powerType
        

        return Action(name, powerType, power)


    def create(self, name):

        if name in self.actions:
            existingPowerType = self.actions[name]
            if existingPowerType is not None:
                raise Exception(f"There exists an action {name} which has a different powerType, {existingPowerType} than the new one None")
            else:
                self.actions[name] = None

        return Action(name)


    def createRandomAction(self):
        self.randomActionLastId += 1
        name = "action-" + str(self.randomActionLastId)
        return self.create(name)


    def createRandomPower(self):
        self.randomActionLastId += 1
        name = "power-" + str(self.randomActionLastId)
        powerType = random.choice(list(PowerType))
        return self.createPower(name, powerType, random.randint(1, 100))


    def createRandom(self):

        if np.random.random_sample() > 0.7:
            # create an action
            return self.createRandomAction()

        else:
            # create a power
            return self.createRandomPower()


    