from game.board import Board
from game.change_position import ChangePosition
from game.direction import Direction
from game.move import Move
import unittest

class test_move(unittest.TestCase):
    def test_start_position_is_known(self):
        board = Board({"columns":8, "rows":8})
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        move = Move(change_position, current_position,board)

        self.assertEqual(move.description(), "You have started on square {}:{}, what's your move?".format(current_position["x"], current_position["y"]))
    
    def test_can_move_up(self):
        board = Board({"columns":8, "rows":8})
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        move = Move(change_position, current_position, board)
        move.direction(Direction.up)

        self.assertEqual(move.description(), "You are now on square 1:2, what's your move?")

    def test_can_move_down(self):
        board = Board({"columns":8, "rows":8})
        current_position = {"x":1, "y":2}
        change_position = ChangePosition()
        move = Move(change_position,current_position,board)
        move.direction(Direction.down)

        self.assertEqual(move.description(), "You are now on square 1:1, what's your move?")
    
    def test_can_move_right(self):
        board = Board({"columns":8, "rows":8})
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        move = Move(change_position, current_position,board)
        move.direction(Direction.right)

        self.assertEqual(move.description(), "You are now on square 2:1, what's your move?")
    
    def test_can_move_left(self):
        board = Board({"columns":8, "rows":8})
        current_position = {"x":2, "y":1}
        change_position = ChangePosition()
        move = Move(change_position,current_position,board)
        move.direction(Direction.left)

        self.assertEqual(move.description(), "You are now on square 1:1, what's your move?")
    
    def test_cannot_move_off_board_up(self):
        board = Board({"columns":1, "rows":1})
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        move = Move(change_position,current_position,board)
        move.direction(Direction.up)

        self.assertEqual(move.description(), "This move is invalid, please try again")
    
    def test_cannot_move_off_board_down(self):
        board = Board({"columns":1, "rows":1})
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        move = Move(change_position,current_position,board)
        move.direction(Direction.down)

        self.assertEqual(move.description(), "This move is invalid, please try again")
    
    def test_cannot_move_off_board_left(self):
        board = Board({"columns":1, "rows":1})
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        move = Move(change_position,current_position,board)
        move.direction(Direction.left)

        self.assertEqual(move.description(), "This move is invalid, please try again")
    
    def test_cannot_move_off_board_right(self):
        board = Board({"columns":1, "rows":1})
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        move = Move(change_position,current_position,board)
        move.direction(Direction.right)

        self.assertEqual(move.description(), "This move is invalid, please try again")
    