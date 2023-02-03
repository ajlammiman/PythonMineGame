from enum import Enum, auto
from game.change_position import ChangePosition

class Direction(Enum):
    up = auto()
    down = auto()
    left = auto()
    right = auto()

class Move():
    ___change_position = None
    ___move_text = "You are now on square {}:{}, what's your move?"

    def __init__(self, change_position: ChangePosition):
        self.___change_position = change_position

    def description(self):
        return self.___move_text.format(self.___change_position.position()["x"], self.___change_position.position()["y"])
    
    def direction(self, direction: Direction):
        if (direction == Direction.up):
            self.___change_position.up()
        elif (direction == Direction.down):
            self.___change_position.down()    
        elif (direction == Direction.right):
            self.___change_position.right()
        elif (direction == Direction.left):
            self.___change_position.left()

        return self.___move_text.format(self.___change_position.position()["x"], self.___change_position.position()["y"])