class ChangePosition:
    def up(self, current_position: dict):
        return {"x":current_position["x"], "y": current_position["y"] +1}

    def down(self, current_position: dict):
        return {"x":current_position["x"], "y": current_position["y"] -1}
    
    def left(self, current_position: dict):
        return {"x":current_position["x"] -1, "y": current_position["y"]}

    def right(self, current_position):
        return {"x":current_position["x"] +1, "y": current_position["y"]}
