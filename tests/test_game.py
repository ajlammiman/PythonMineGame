from game.game import Game
import unittest

class test_game(unittest.TestCase):
    def test_game_has_start_message(self):
        game = Game()
        self.assertEqual(game.output(), '''Welcome to the Game, you must reach the other side. Try not to die! Press S to start.\n 
        The board is 8x8, you must cross to the other side but avoid the mines! 3 mines and you lose.\n
        move up with W, down with X, left with A and right with D.''')
    
    def test_game_can_be_started_with_default_starting_position(self):
        game = Game()
        game.start()

        self.assertEqual(game.output(), "You have started on sqare 1:1, what's your move?")

    def test_player_start_position_can_be_defined(self):
        start = {"x":1, "y":2}
        game = Game(start)
        game.start()
       
        self.assertEqual(game.output(), "You have started on sqare 1:2, what's your move?")
    
    def test_player_can_move_up(self):
        game = Game()
        game.start()

        self.assertEqual(game.output(), "You have started on sqare 1:1, what's your move?")

        game.player_move_up()
       
        self.assertEqual(game.output(), "You are now on square 1:2, what's your move?")
    
    def test_player_can_move_right(self):
        game = Game()
        game.start()

        self.assertEqual(game.output(), "You have started on sqare 1:1, what's your move?")

        game.player_move_right()
       
        self.assertEqual(game.output(), "You are now on square 2:1, what's your move?")
    
    def test_player_can_move_left(self):
        start = {"x":1, "y":2}
        game = Game(start)
        game.start()
       
        self.assertEqual(game.output(), "You have started on sqare 1:2, what's your move?")

        game.player_move_left()
       
        self.assertEqual(game.output(), "You are now on square 1:1, what's your move?")

    def test_player_can_move_down(self):
        start = {"x":2, "y":1}
        game = Game(start)
        game.start()
       
        self.assertEqual(game.output(), "You have started on sqare 2:1, what's your move?")

        game.player_move_down()
       
        self.assertEqual(game.output(), "You are now on square 1:1, what's your move?")
    
