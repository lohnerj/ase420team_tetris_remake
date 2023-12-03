import unittest
import pygame
from final_tetris_refactored import Board, BrightTetrisColors


class TestBoard(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.empty_board = Board(color_scheme=BrightTetrisColors())
        

    def test_score_increment_empty_board(self):
        self.assertEqual(self.empty_board.score, 0)

    def test_score_increment_single_row(self):
        # Assuming you have a method to add a row to the board
        self.empty_board.add_to_field([1, 1, 1, 1])
        self.empty_board.break_lines()
        self.assertEqual(self.empty_board.score, 110)

    def test_score_increment_multiple_rows(self):
        # Assuming you have a method to add multiple rows to the board
        self.empty_board.add_to_field([1, 1, 1, 1])
        self.empty_board.add_to_field([1, 1, 1, 1])
        self.empty_board.break_lines()
        self.assertEqual(self.empty_board.score, 210)

    def test_score_increment_no_full_rows(self):
        # No full rows, score should remain 0
        self.empty_board.add_to_field([1, 0, 1, 0])
        self.empty_board.break_lines()
        self.assertEqual(self.empty_board.score, 0)


if __name__ == '__main__':
    unittest.main()
