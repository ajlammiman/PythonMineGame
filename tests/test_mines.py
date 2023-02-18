import unittest
from unittest.mock import patch
from game.board import Board
from game.mines import Mines

class test_mines(unittest.TestCase):
    
    def test_if_no_mines_defined_default_number_generated(self):
        mines_mock = [{"x":1, "y":1},{"x":1, "y":2},{"x":1, "y":3},{"x":1, "y":4},{"x":1, "y":5},{"x":1, "y":6},{"x":1, "y":7},{"x":1, "y":8}]

        with patch.object(Mines,"_Mines__generate_mines", lambda self, number_of_mines: mines_mock):     
            mines = Mines()
            self.assertEqual(len(mines._Mines___mines), 8)
    
    def test_number_of_mines_defined_are_same_as_generated(self):
        number_of_mines = 9
        mines_mock = [{"x":1, "y":1},{"x":1, "y":2},{"x":1, "y":3},{"x":1, "y":4},{"x":1, "y":5},{"x":1, "y":6},{"x":1, "y":7},{"x":1, "y":8},{"x":1, "y":9}]

        with patch.object(Mines,"_Mines__generate_mines", lambda self, number_of_mines: mines_mock):     
            mines = Mines(number_of_mines)
            self.assertEqual(len(mines._Mines___mines), number_of_mines)
        
    def test_informs_if_mine_is_present(self):
        mined_location = {"x":1,"y":1}
        number_of_mines = 1
        with patch.object(Mines,"check_for_mine", lambda self, check_position: True):     
            mines = Mines(number_of_mines)
            self.assertEqual(mines.check_for_mine(mined_location), True)
    
    def test_informs_if_mine_is_not_present(self):
        mined_location = {"x":1,"y":1}
        number_of_mines = 1
        with patch.object(Mines,"check_for_mine", lambda self, check_position: False):     
            mines = Mines(number_of_mines)
            self.assertEqual(mines.check_for_mine(mined_location), False)