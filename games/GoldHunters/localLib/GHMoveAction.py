from library.PowerType import PowerType

class GHMoveAction(ABC):

    def __init__(self, name, direction, powerType:PowerType=None, power:int=0):
        
        self.name = name
        self.direction = direction
        self.powerType = powerType
        self.power = power  

        pass


    def __str__(self):

        return f"[name: {self.name}, direction: {self.direction}, powerType: {self.powerType}, power: {self.power}]"

