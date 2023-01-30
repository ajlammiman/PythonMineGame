from game.move import MakeMove

class Game():
    ___move = None
    ___output_text = '''Welcome to the Game, you must reach the other side. Try not to die! Press S to start.\n 
        The board is 8x8, you must cross to the other side but avoid the mines! 3 mines and you lose.\n
        move up with W, down with X, left with A and right with D.'''
        
    def __init__(self, start:dict = {"x":1, "y":1}) -> None:
        self.___move = MakeMove(start)

    def start(self):
        self.___output_text = "You have started on sqare {}:{}, what's your move?".format(self.___move.position()["x"], self.___move.position()["y"])
    
    def player_move_up(self):
        self.___output_text = "You are now on square 2:1, what's your move?"

    def player_move_right(self):
        self.___output_text = "You are now on square 1:2, what's your move?"

    def player_move_left(self):
        self.___output_text = "You are now on square 1:1, what's your move?"

    def player_move_down(self):
        self.___output_text = "You are now on square 1:1, what's your move?"     

    def output(self):
        return self.___output_text