import random 

class Mines:
    ___mines = []

    def __init__(self, number_of_mines: int = 8) -> None:
        self.___mines = self.__generate_mines(number_of_mines)

    def __generate_mines(self, number_of_mines: int):
        return [({"x": int(random.random()),"y": int(random.random())}) for _ in range(number_of_mines)]
    
    def check_for_mine(self, check_position:dict):
        return True if check_position in self.___mines else False