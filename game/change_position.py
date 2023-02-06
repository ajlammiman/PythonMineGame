from game.direction import Direction


class ChangePosition:
    def up(self, current_position: dict):
        return {"x":current_position["x"], "y": current_position["y"] +1}

    def down(self, current_position: dict):
        return {"x":current_position["x"], "y": current_position["y"] -1}
    
    def left(self, current_position: dict):
        return {"x":current_position["x"] -1, "y": current_position["y"]}

    def right(self, current_position):
        return {"x":current_position["x"] +1, "y": current_position["y"]}
    
    def change(self, current_position: dict, direction: Direction):
        if (direction == Direction.up):
            return {"x":current_position["x"], "y": current_position["y"] +1}
        
        if (direction == Direction.down):
            return {"x":current_position["x"], "y": current_position["y"] -1}

        if (direction == Direction.left):
            return {"x":current_position["x"] -1, "y": current_position["y"]}
        
        if (direction == Direction.right):
            return {"x":current_position["x"] +1, "y": current_position["y"]}