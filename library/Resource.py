from abc import ABC, abstractmethod

from library.ResourceType import ResourceType


class Resource(ABC):

    def __init__(self, name, quantity, type=ResourceType.GENERIC, unit='piece', reusable=False, relocatable=False):
        self.name = name
        self.quantity = quantity
        self.type = type
        self.unit = unit
        self.reusable = reusable
        self.relocatable = relocatable

        pass


    def dec(self, amount):
        self.quantity -= amount

        return


    def inc(self, amount):
        self.quantity += amount

        return

    @abstractmethod
    def use(self):
        pass
