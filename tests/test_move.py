from game.board import Board
from game.change_position import ChangePosition
from game.move import Direction, Move
import unittest

class test_move(unittest.TestCase):
    def test_start_position_is_known(self):
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        move = Move(change_position, current_position)

        self.assertEqual(move.description(), "You have started on square {}:{}, what's your move?".format(current_position["x"], current_position["y"]))
    
    def test_can_move_up(self):
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        move = Move(change_position, current_position)
        move.direction(Direction.up)

        self.assertEqual(move.description(), "You are now on square 1:2, what's your move?")

    def test_can_move_down(self):
        current_position = {"x":1, "y":2}
        change_position = ChangePosition()
        move = Move(change_position,current_position)
        move.direction(Direction.down)

        self.assertEqual(move.description(), "You are now on square 1:1, what's your move?")
    
    def test_can_move_right(self):
        current_position = {"x":1, "y":1}
        change_position = ChangePosition()
        move = Move(change_position, current_position)
        move.direction(Direction.right)

        self.assertEqual(move.description(), "You are now on square 2:1, what's your move?")
    
    def test_can_move_left(self):
        current_position = {"x":2, "y":1}
        change_position = ChangePosition()
        move = Move(change_position,current_position)
        move.direction(Direction.left)

        self.assertEqual(move.description(), "You are now on square 1:1, what's your move?")
    
   