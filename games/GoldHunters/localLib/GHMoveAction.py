from library.PowerType import PowerType
from library.Action import Action
from games.GoldHunters.localLib.GHActionType import GHActionType

class GHMoveAction(Action):

    def __init__(self, actionType):
        
        super().__init__(actionType.name)
        self.direction = actionType.value
        pass


    def __str__(self):

        baseStr = super().__str__()
        return(
            f"{baseStr}\n"
            f"direction: {self.direction}"
        )
    

        
