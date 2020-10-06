# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_if_word_valid(self):
        new_game = Game()
        new_game.grid = ['S', 'O', 'L', 'R', 'E', 'U', 'T', 'Y']
        self.assertEqual(new_game.is_valid('ROSULT'), False)
        self.assertEqual(new_game.grid, ['S', 'O', 'L', 'R', 'E', 'U', 'T', 'Y'])

    def test_word_is_valid(self):
        new_game = Game()
        new_game.grid = ['S', 'O', 'L', 'R', 'E', 'U', 'T', 'F']
        self.assertEqual(new_game.is_valid('RESULT'), True)
        self.assertEqual(new_game.grid, ['S', 'O', 'L', 'R', 'E', 'U', 'T', 'Y'])

    def test_invalid_word_with_list(self):
        new_game = Game()
        new_game.grid = ['S', 'O', 'L', 'R', 'E', 'U', 'T', 'Y']
        self.assertEqual(new_game.is_valid('WAGON'), False)
        self.assertEqual(new_game.grid, ['S', 'O', 'L', 'R', 'E', 'U', 'T', 'Y'])

    def test_empty_word(self):
        new_game = Game()
        self.assertEqual(new_game.is_valid(''), False)
