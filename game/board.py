class Board():
    ___board = [] 
    ___dimensions = None

    def __init__(self, dimensions:dict) -> None:
        self.___board = self.___generate_board(dimensions)
        self.___dimensions = dimensions
    
    def get_board_dimensions(self):
        return self.___dimensions
    
    def is_valid_move(self, position: dict):
        return self.___board.__contains__(position)

    def ___generate_board(self, dimensions:dict):
        new_board = []
        for row in range(dimensions["rows"]):
            for column in range(dimensions["columns"]):
                new_board.append({"x": column + 1, "y": row + 1})
        return new_board