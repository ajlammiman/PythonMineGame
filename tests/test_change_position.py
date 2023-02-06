from game.direction import Direction
from game.change_position import ChangePosition
import unittest

class test_change_position(unittest.TestCase):
    def test_can_change_position_up(self):
        starting_position = {"x":1, "y":1}
        change_position = ChangePosition()
        
        new_position = change_position.change(starting_position, Direction.up)
       
        self.assertEqual(new_position, {"x":1, "y":2})
    

    def test_can_change_position_down(self):
        starting_position = {"x":1, "y":2}
        change_position = ChangePosition()

        new_position = change_position.change(starting_position, Direction.down)
       
        self.assertEqual(new_position, {"x":1, "y":1})
    
    def test_can_change_position_left(self):
        starting_position = {"x":2, "y":1}
        change_position = ChangePosition()

        new_position = change_position.change(starting_position, Direction.left)
       
        self.assertEqual(new_position, {"x":1, "y":1})

    def test_can_chnage_position_right(self):
        starting_position = {"x":1, "y":1}
        change_position = ChangePosition()

        new_position = change_position.change(starting_position, Direction.right)
       
        self.assertEqual(new_position, {"x":2, "y":1})

    
