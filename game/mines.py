import random 
from game.board import Board
from game.direction import Direction


class Mines:
    ___mines = []

    def __init__(self, board: Board, number_of_mines: int = 8) -> None:
        self.___mines = self.__generate_mines(number_of_mines)

    def __generate_mines(self, number_of_mines: int):
        return [(int(random.random()*2.0), int(random.random()*2.0)) for _ in range(number_of_mines)]

    def check_for_mine(self, position:dict, direction: Direction):
        return ""