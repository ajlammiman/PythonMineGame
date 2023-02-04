class Board():
    ___dimensions = None

    def __init__(self, dimensions:dict) -> None:
        self.___dimensions = dimensions
    
    def getBoardDimensions(self):
        return self.___dimensions
