import unittest
import pygame
from final_tetris_refactored import Board, BrightTetrisColors


class TestLevelIncrementation(unittest.TestCase):

    def test_initial_level(self):
        board = Board(color_scheme=BrightTetrisColors())
        self.assertEqual(board.get_level(), 1)

    def test_level_incrementation(self):
        board = Board(color_scheme=BrightTetrisColors())

        self.assertEqual(board.get_level(), 1)

        board.update_level(500)

        self.assertEqual(board.get_level(), 2)

        board.update_level(1000)

        self.assertEqual(board.get_level(), 3)


if __name__ == '__main__':
    unittest.main()
