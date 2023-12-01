import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import final_tetris_refactored as ftr


class TestFiguresLength(unittest.TestCase):
    #test that ever index in the four block figures array has 4 values
    def test_each_figure_has_four_blocks_in_four_block_figure(self):
        four_figures_array = ftr.MakeFourBlockFigure(3, 0, ftr.TraditionalTetrisColors()).figures #using random color scheme for the sake of testing.
        for figures in four_figures_array:
            amount_of_rotations = len(figures)
            for rotation in range(0, amount_of_rotations):
                self.assertEqual(len(figures[rotation]), 4)

    #test that ever index in the five block figures array has 5 values
    def test_each_figure_had_five_blocks_in_five_block_figure(self):
        five_figure_array = ftr.MakeFiveBlockFigure(3,0, ftr.TraditionalTetrisColors()).figures
        for figures in five_figure_array:
            amount_of_rotations = len(figures)
            for rotation in range(0, amount_of_rotations):
                self.assertEqual(len(figures[rotation]), 5)

    #test that ever index in the six block figures array has 6 values
    def test_each_figure_had_six_blocks_in_six_block_figure(self):
        six_figure_array = ftr.MakeSixBlockFigure(3,0, ftr.TraditionalTetrisColors()).figures
        for figures in six_figure_array:
            amount_of_rotations = len(figures)
            for rotation in range(0, amount_of_rotations):
                self.assertEqual(len(figures[rotation]), 6)


if __name__ == '__main__':
    unittest.main()
