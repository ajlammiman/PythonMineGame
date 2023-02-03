from game.change_position import ChangePosition
import unittest

class test_change_position(unittest.TestCase):
    def test_position_is_known_before_move(self):
        current_position = {"x":1, "y":1}
        change_position = ChangePosition(current_position)

        self.assertEqual(change_position.position(), current_position)
    
    
    def test_can_change_position_up(self):
        current_position = {"x":1, "y":1}
        change_position = ChangePosition(current_position)

        change_position.up()
       
        self.assertEqual(change_position.position(), {"x":1, "y":2})
    

    def test_can_change_position_down(self):
        current_position = {"x":1, "y":2}
        change_position = ChangePosition(current_position)

        change_position.down()
       
        self.assertEqual(change_position.position(), {"x":1, "y":1})
    
    def test_can_change_position_left(self):
        current_position = {"x":2, "y":1}
        change_position = ChangePosition(current_position)

        change_position.left()
       
        self.assertEqual(change_position.position(), {"x":1, "y":1})

    def test_can_chnage_position_right(self):
        current_position = {"x":1, "y":1}
        change_position = ChangePosition(current_position)

        change_position.right()
       
        self.assertEqual(change_position.position(), {"x":2, "y":1})

    
