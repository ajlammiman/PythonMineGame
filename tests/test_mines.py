import unittest
from unittest.mock import patch
from game.mines import Mines

class test_mines(unittest.TestCase):
    
    def test_if_no_mines_defined_default_number_generated(self):
        mines = Mines()
        self.assertEqual(len(mines._Mines___mines), 8)


    def test_mines_are_returned_as_a_list_of_coordinates_matching_expected_number_of_mines(self):
        number_of_mines = 2
        mined_locations = [{"x":1,"y":1},{"x":1,"y":1}]
        with patch("game.mines.random.random", lambda : 1):     
            mines = Mines(2)
            self.assertEqual(len(mines._Mines___mines), number_of_mines)
            self.assertEqual(mines._Mines___mines, mined_locations)
    
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