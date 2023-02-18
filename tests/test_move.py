from game.board import Board
from game.change_position import ChangePosition
from game.direction import Direction
from game.mines import Mines
from game.move import Move
import unittest

class test_move(unittest.TestCase):
    def test_start_position_is_known(self):
        board = Board({"columns":8, "rows":8})
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        mines = Mines()
        move = Move(change_position, current_position,board, mines)

        self.assertEqual(move.description(), "You have started on square {}:{}, what's your move?".format(current_position["x"], current_position["y"]))
    
    def test_can_make_a_move(self):
        board = Board({"columns":8, "rows":8})
        current_position = {"x":1, "y":1}
        mines = Mines()
        change_position = ChangePosition()
        move = Move(change_position, current_position, board, mines)
        move.direction(Direction.up)

        self.assertEqual(move.description(), "You are now on square 1:2, what's your move?")
    
    def test_cannot_move_off_board(self):
        board = Board({"columns":1, "rows":1})
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        mines = Mines()
        move = Move(change_position, current_position,board, mines)
        move.direction(Direction.up)

        self.assertEqual(move.description(), "This move is invalid, please try again")   
    