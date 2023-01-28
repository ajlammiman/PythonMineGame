class MakeMove:
    ___position = None

    def __init__(self, current_position: dict):
        self.___position = current_position

    def up(self):
        self.___position = {"x":self.___position["x"], "y": self.___position["y"] +1}

    def down(self):
        self.___position = {"x":self.___position["x"], "y": self.___position["y"] -1}
    
    def left(self):
        self.___position = {"x":self.___position["x"] -1, "y": self.___position["y"]}


    def position(self):
        return self.___position