from abc import ABC, abstractmethod
from library.PowerType import PowerType

class Action(ABC):

    def __init__(self, name, powerType:PowerType=None, power:int=None):
        self.name = name
        self.powerType = powerType
        self.power = power  
