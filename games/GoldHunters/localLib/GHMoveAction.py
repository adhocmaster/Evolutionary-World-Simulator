from library.PowerType import PowerType
from library.Action import Action

class GHMoveAction(Action):

    def __init__(self, name, direction):
        
        super().__init__(name)
        self.direction = direction
        pass


    def __str__(self):

        baseStr = super().__str__()
        return(
            f"{baseStr}\n"
            f"direction: {self.direction}"
        )
        
