import unittest
import pygame
from final_tetris_refactored import Board, BrightTetrisColors


class TestBoard(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.empty_board = Board(color_scheme=BrightTetrisColors())

    def test_score_increment_empty_board(self):
        print("Inital score: ", self.empty_board.score)
        self.assertEqual(self.empty_board.score, 0)

    def test_score_increment_single_row(self):
        print("Before adding row:", self.empty_board.score)
        self.empty_board.add_to_field([1, 1, 1, 1])
        print("After adding row:", self.empty_board.score)
        self.empty_board.break_lines()
        print("After breaking lines:", self.empty_board.score)
        self.assertEqual(self.empty_board.score, 10)

    def test_score_increment_multiple_rows(self):
        print("Before adding row:", self.empty_board.score)
        self.empty_board.add_to_field([1, 1, 1, 1])
        self.empty_board.add_to_field([1, 1, 1, 1])
        print("After adding rows:", self.empty_board.score)
        self.empty_board.break_lines()
        self.empty_board.break_lines()
        print("After breaking lines:", self.empty_board.score)
        self.assertEqual(self.empty_board.score, 20)

    def test_score_increment_no_full_rows(self):
        print("Before adding incomplete row:", self.empty_board.score)
        self.empty_board.add_to_field([1, 0, 1, 0])
        print("After adding incomplete row:", self.empty_board.score)
        self.empty_board.break_lines()
        print("After breaking lines (no full rows):", self.empty_board.score)
        self.assertEqual(self.empty_board.score, 10)


if __name__ == '__main__':
    unittest.main()
