import unittest
from game.board import Board

class test_board(unittest.TestCase):
    def test_board_can_tell_you_its_dimensions(self):
        dimensions ={"columns":8, "rows":8}
        board = Board(dimensions)

        self.assertEqual(board.get_board_dimensions(), dimensions)

    def test_board_can_tell_you_a_move_stays_on_the_board(self):
        dimensions ={"columns":2, "rows":1}
        board = Board(dimensions)
        is_valid = board.is_valid_move({"x":2,"y":1})
        self.assertEqual(is_valid, True)
    
    def test_board_can_tell_you_a_move_goes_off_the_board(self):
        dimensions ={"columns":1, "rows":1}
        board = Board(dimensions)
        is_valid = board.is_valid_move({"x":0,"y":1})
        self.assertEqual(is_valid, False)
