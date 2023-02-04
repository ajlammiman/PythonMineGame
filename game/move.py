from enum import Enum, auto
from game.board import Board
from game.change_position import ChangePosition

class Direction(Enum):
    up = auto()
    down = auto()
    left = auto()
    right = auto()

class Move():
    ___start_text = "You have started on square {}:{}, what's your move?"
    ___move_text = "You are now on square {}:{}, what's your move?"
    ___board = None
    ___position = None
    ___change_position = None
    ___description = ""

    def __init__(self, change_position: ChangePosition, position: dict):
        self.___position = position
        self.___change_position = change_position
        self.___description = self.___start_text.format(self.___position["x"], self.___position["y"])

    def description(self):
        return self.___description
    
    def direction(self, direction: Direction):
        if (direction == Direction.up):
            self.___position = self.___change_position.up(self.___position)
            self.___description = self.___move_text.format(self.___position["x"], self.___position["y"])
        elif (direction == Direction.down):
            self.___position = self.___change_position.down(self.___position)
            self.___description = self.___move_text.format(self.___position["x"], self.___position["y"])
        elif (direction == Direction.right):
            self.___position = self.___change_position.right(self.___position)
            self.___description = self.___move_text.format(self.___position["x"], self.___position["y"])
        elif (direction == Direction.left):
            self.___position = self.___change_position.left(self.___position)
            self.___description = self.___move_text.format(self.___position["x"], self.___position["y"])
       
       