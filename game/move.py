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

    def __init__(self, change_position: ChangePosition, position: dict, board: Board):
        self.___invalid_move = "This move is invalid, please try again"
        self.___position = position
        self.___change_position = change_position
        self.___board = board
        self.___description = self.___start_text.format(self.___position["x"], self.___position["y"])

    def description(self):
        return self.___description
    
    def direction(self, direction: Direction):
        if (direction == Direction.up):
            new_position = self.___change_position.up(self.___position)
            if (self.___board.is_valid_move(new_position)):
                self.___description = self.___move_text.format(new_position["x"], new_position["y"])
            else:
                self.___description = self.___invalid_move
        elif (direction == Direction.down):
            new_position = self.___change_position.down(self.___position)
            if (self.___board.is_valid_move(new_position)):
                self.___description = self.___move_text.format(new_position["x"], new_position["y"])
            else:
                self.___description = self.___invalid_move
        elif (direction == Direction.right):
            new_position = self.___change_position.right(self.___position)
            if (self.___board.is_valid_move(new_position)):
                self.___description = self.___move_text.format(new_position["x"], new_position["y"])
            else:
                self.___description = self.___invalid_move
        elif (direction == Direction.left):
            new_position = self.___change_position.left(self.___position)
            if (self.___board.is_valid_move(new_position)):
                self.___description = self.___move_text.format(new_position["x"], new_position["y"])
            else:
                self.___description = self.___invalid_move
