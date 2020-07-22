from enum import Enum

class GHActionType(Enum):
    
    MoveUp = (0, 1)
    MoveDown = (0, -1)
    MoveLeft = (-1, 0)
    MoveRight = (1, 0) 
    MoveUpLeft = (-1, 1)
    MoveUpRight = (1, 1)
    MoveDownLeft = (-1, -1)
    MoveDownRight = (1, -1)
    Dig = 'Dig'
    Rob = 'Rob'

