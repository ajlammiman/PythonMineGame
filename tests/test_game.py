from game.board import Board
from game.change_position import ChangePosition
from game.game import Game
import unittest

from game.mines import Mines

class test_game(unittest.TestCase):
    def test_game_start_message_displays_size_of_board(self):
        board_size = {"columns":2, "rows":2}
        board = Board(board_size)
        mines = Mines()
        change_position = ChangePosition()
        game = Game(board, mines, change_position)
        self.assertEqual(game.output(), '''Welcome to the Game, you must reach the other side. Try not to die! Press S to start.\n 
        The board is {}x{}, you must cross to the other side but avoid the mines! 3 mines and you lose.\n
        move up with W, down with X, left with A and right with D.'''.format(board_size["columns"],board_size["rows"]))
    
    def test_game_can_be_started_with_default_starting_position(self):
        board = Board({"columns":8, "rows":8})
        mines = Mines()
        change_position = ChangePosition()
        game = Game(board, mines, change_position)
        game.start()

        self.assertEqual(game.output(), "You have started on square 1:1, what's your move?")

    def test_player_start_position_can_be_defined(self):
        board = Board({"columns":8, "rows":8})
        start = {"x":1, "y":2}
        mines = Mines()
        change_position = ChangePosition()
        game = Game(board, mines, change_position, start)
        game.start()
       
        self.assertEqual(game.output(), "You have started on square 1:2, what's your move?")
    
    def test_player_can_move_up(self):
        board = Board({"columns":8, "rows":8})
        mines = Mines()
        change_position = ChangePosition()
        game = Game(board, mines, change_position)
        
        game.start()

        self.assertEqual(game.output(), "You have started on square 1:1, what's your move?")

        game.player_move_up()
       
        self.assertEqual(game.output(), "You are now on square 1:2, what's your move?")
    
    def test_player_can_move_right(self):
        board = Board({"columns":8, "rows":8})
        mines = Mines()
        change_position = ChangePosition()
        game = Game(board, mines, change_position)
        
        game.start()

        self.assertEqual(game.output(), "You have started on square 1:1, what's your move?")

        game.player_move_right()
       
        self.assertEqual(game.output(), "You are now on square 2:1, what's your move?")
    
    def test_player_can_move_left(self):
        board = Board({"columns":8, "rows":8})
        start = {"x":2, "y":1}
        mines = Mines()
        change_position = ChangePosition()
        game = Game(board, mines, change_position, start)
        
        game.start()
       
        self.assertEqual(game.output(), "You have started on square 2:1, what's your move?")

        game.player_move_left()
       
        self.assertEqual(game.output(), "You are now on square 1:1, what's your move?")

    def test_player_can_move_down(self):
        board = Board({"columns":8, "rows":8})
        start = {"x":1, "y":2}
        mines = Mines()
        change_position = ChangePosition()
        game = Game(board, mines, change_position, start)
        
        game.start()
       
        self.assertEqual(game.output(), "You have started on square 1:2, what's your move?")

        game.player_move_down()
       
        self.assertEqual(game.output(), "You are now on square 1:1, what's your move?")
    
