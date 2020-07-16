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
    MoveDownRight = 'MoveDownRight'

    # GHMoveAction('MoveLeft', (-1, 0)), 
    # GHMoveAction('MoveRight', (1, 0)), 
    # GHMoveAction('MoveUpLeft', (-1, 1)),
    # GHMoveAction('MoveUpRight', (1, 1)), 
    # GHMoveAction('MoveDownLeft', (-1, -1)), 
    # GHMoveAction('MoveDownRight', (1, -1)),
    # Action("dig"),
    # Action("rob")
