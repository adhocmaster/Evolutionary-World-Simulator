from abc import ABC, abstractmethod

class Resource(ABC):

    def __init__(self, name, quantity, type='discrete', unit='piece', reusable=False, relocatable=False):
        self.name = name
        self.quantity = quantity
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

    