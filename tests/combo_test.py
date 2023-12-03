import unittest
from final_tetris_refactored import Board, BrightTetrisColors


class TestComboCount(unittest.TestCase):
    def test_combo_count_increment(self):
        board = Board(color_scheme=BrightTetrisColors())

        self.assertEqual(board.combo_count, 0)

        board.update_combo()

        self.assertEqual(board.combo_count, 1)

    def test_combo_count_reset(self):

        board = Board(color_scheme=BrightTetrisColors())

        board.update_combo()

        board.reset_combo()

        self.assertEqual(board.combo_count, 0)

    def test_combo_count_after_break_lines(self):

        board = Board(color_scheme=BrightTetrisColors())

        board.break_lines()


if __name__ == '__main__':
    unittest.main()
