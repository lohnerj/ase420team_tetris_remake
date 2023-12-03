import unittest
import pygame
from final_tetris_refactored import Board


class TestLevelIncrementation(unittest.TestCase):

    def test_initial_level(self):
        board = Board(color_scheme=None)
        self.assertEqual(board.get_level(), 1)

    def test_level_incrementation(self):
        board = Board(color_scheme=None)

        self.assertEqual(board.get_level(), 1)

        board.update_level(2500)

        self.assertEqual(board.get_level(), 2)

        board.update_level(5000)

        self.assertEqual(board.get_level(), 3)


if __name__ == '__main__':
    unittest.main()
