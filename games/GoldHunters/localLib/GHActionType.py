from enum import Enum

class GHActionType(Enum):
    # TODO
    MoveUp = 'MoveUp',
    MoveDown = 'MoveDown',
    MoveLeft = 'MoveLeft',
    MoveRight = 'MoveRight', 
    MoveUpLeft = 'MoveUpLeft',
    MoveUpRight = 'MoveUpRight',
    MoveDownLeft = 'MoveDownLeft',
    MoveDownRight = 'MoveDownRight',
    Dig = 'Dig',
    Rob = 'Rob'

