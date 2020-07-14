from library.PowerType import PowerType

class Action():

    def __init__(self, name, powerType:PowerType=None, power:int=0):
        
        self.name = name
        self.powerType = powerType
        self.power = power  

        pass


    def __str__(self):

        return f"[name: {self.name}, powerType: {self.powerType}, power: {self.power}]"

