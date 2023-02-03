from game.change_position import ChangePosition
import unittest

class test_change_position(unittest.TestCase):
    def test_position_is_known_before_move(self):
        current_position = {"x":1, "y":1}
        move = ChangePosition(current_position)

        self.assertEqual(move.position(), current_position)
    
    
    def test_can_change_position_up(self):
        current_position = {"x":1, "y":1}
        move = ChangePosition(current_position)

        move.up()
       
        self.assertEqual(move.position(), {"x":1, "y":2})
    

    def test_can_change_position_down(self):
        current_position = {"x":1, "y":2}
        move = ChangePosition(current_position)

        move.down()
       
        self.assertEqual(move.position(), {"x":1, "y":1})
    
    def test_can_change_position_left(self):
        current_position = {"x":2, "y":1}
        move = ChangePosition(current_position)

        move.left()
       
        self.assertEqual(move.position(), {"x":1, "y":1})

    def test_can_chnage_position_right(self):
        current_position = {"x":1, "y":1}
        move = ChangePosition(current_position)

        move.right()
       
        self.assertEqual(move.position(), {"x":2, "y":1})

    
