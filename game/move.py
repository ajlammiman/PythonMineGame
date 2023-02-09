from game.board import Board
from game.change_position import ChangePosition
from game.direction import Direction
from game.mines import Mines

class Move():
    ___start_text = "You have started on square {}:{}, what's your move?"
    ___move_text = "{}You are now on square {}:{}, what's your move?"
    ___board = None
    ___position = None
    ___change_position = None
    ___mines = None
    ___description = ""

    def __init__(self, change_position: ChangePosition, position: dict, board: Board, mines: Mines):
        self.___invalid_move = "This move is invalid, please try again"
        self.___position = position
        self.___change_position = change_position
        self.___board = board
        self.___mines = mines
        self.___description = self.___start_text.format(self.___position["x"], self.___position["y"])

    def description(self):
        return self.___description
    
    def direction(self, direction: Direction):
        new_position = self.___change_position.change(self.___position, direction)
        mine_message = self.___mines.check_for_mine(self.___position, direction)

        if (self.___board.is_valid_move(new_position)):
            self.___description = self.___move_text.format(mine_message, new_position["x"], new_position["y"])
        else:
            self.___description = self.___invalid_move       