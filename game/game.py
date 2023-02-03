from game.change_position import ChangePosition
from game.move import Direction, Move

class Game():
    ___move = None
    ___output_text = '''Welcome to the Game, you must reach the other side. Try not to die! Press S to start.\n 
        The board is 8x8, you must cross to the other side but avoid the mines! 3 mines and you lose.\n
        move up with W, down with X, left with A and right with D.'''
        
    def __init__(self, start:dict = {"x":1, "y":1}) -> None:
       change_position = ChangePosition(start)
       self.___move = Move(change_position)

    def start(self):
        self.___output_text = self.___move.description()
    
    def player_move_up(self):
        self.___move.direction(Direction.up)
        self.___output_text = self.___move.description()

    def player_move_right(self):
        self.___move.direction(Direction.right)
        self.___output_text = self.___move.description()

    def player_move_left(self):
        self.___move.direction(Direction.left)
        self.___output_text = self.___move.description()

    def player_move_down(self):
        self.___move.direction(Direction.down)
        self.___output_text = self.___move.description()

    def output(self):
        return self.___output_text

    