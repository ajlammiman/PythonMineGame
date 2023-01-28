from game.move import MakeMove
import unittest

class test_move(unittest.TestCase):
    def test_position_is_known_before_move(self):
        current_position = {"x":1, "y":1}
        move = MakeMove(current_position)

        self.assertEqual(move.position(), current_position)
    
    
    def test_can_move_up(self):
        current_position = {"x":1, "y":1}
        move = MakeMove(current_position)

        move.up()
       
        self.assertEqual(move.position(), {"x":1, "y":2})
    

    def test_can_move_down(self):
        current_position = {"x":1, "y":2}
        move = MakeMove(current_position)

        move.down()
       
        self.assertEqual(move.position(), {"x":1, "y":1})
    