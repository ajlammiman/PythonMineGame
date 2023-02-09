import unittest
from game.board import Board
from game.mines import Mines

class test_mines(unittest.TestCase):
    def test_number_of_mines_defined_are_generated(self):
        number_of_mines = 8
        board = Board({"columns":8, "rows":8})
        mines = Mines(board,number_of_mines)
        self.assertEqual(len(mines._Mines___mines), number_of_mines)