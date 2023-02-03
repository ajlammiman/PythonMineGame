from enum import Enum, auto
from game.change_position import ChangePosition

class Direction(Enum):
    up = auto()
    down = auto()
    left = auto()
    right = auto()

class Move():
    ___start_text = "You have started on square {}:{}, what's your move?"
    ___move_text = "You are now on square {}:{}, what's your move?"
    ___change_position = None
    ___description = ""

    def __init__(self, change_position: ChangePosition):
        self.___change_position = change_position
        self.___description = self.___start_text.format(self.___change_position.position()["x"], self.___change_position.position()["y"])

    def description(self):
        return self.___description
    
    def direction(self, direction: Direction):
        if (direction == Direction.up):
            self.___change_position.up()
            self.___description = self.___move_text.format(self.___change_position.position()["x"], self.___change_position.position()["y"])
        elif (direction == Direction.down):
            self.___change_position.down()
            self.___description = self.___move_text.format(self.___change_position.position()["x"], self.___change_position.position()["y"])    
        elif (direction == Direction.right):
            self.___change_position.right()
            self.___description = self.___move_text.format(self.___change_position.position()["x"], self.___change_position.position()["y"])
        elif (direction == Direction.left):
            self.___change_position.left()
            self.___description = self.___move_text.format(self.___change_position.position()["x"], self.___change_position.position()["y"])

       