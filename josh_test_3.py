import unittest
from final_tetris_refactored import TraditionalTetrisColors, BaseFigure, MakeFourBlockFigure

class TestBaseFigure(unittest.TestCase):
    def test_base_figure_initialization(self):
        color_scheme = TraditionalTetrisColors()
        base_figure = BaseFigure(2, 3, color_scheme)

        self.assertEqual(base_figure.get_shift_x(), 2)
        self.assertEqual(base_figure.get_shift_y(), 3)
        self.assertEqual(base_figure.get_rotation(), 0)
        self.assertIsNotNone(base_figure.get_exact_color())
        self.assertEqual(base_figure.get_color_scheme_name(), color_scheme)

    def test_base_figure_updates(self):
        color_scheme = TraditionalTetrisColors()
        base_figure = BaseFigure(2, 3, color_scheme)

        base_figure.update_shift_x(5)
        base_figure.update_shift_y(7)
        base_figure.update_rotation(2)

        self.assertEqual(base_figure.get_shift_x(), 5)
        self.assertEqual(base_figure.get_shift_y(), 7)
        self.assertEqual(base_figure.get_rotation(), 2)

class TestMakeFourBlockFigure(unittest.TestCase):
    def test_make_four_block_figure_initialization(self):
        color_scheme = TraditionalTetrisColors()
        make_four_block_figure = MakeFourBlockFigure(2, 3, color_scheme)

        self.assertEqual(make_four_block_figure.get_shift_x(), 2)
        self.assertEqual(make_four_block_figure.get_shift_y(), 3)
        self.assertEqual(make_four_block_figure.get_rotation(), 0)
        self.assertIsNotNone(make_four_block_figure.get_exact_color())
        self.assertEqual(make_four_block_figure.get_color_scheme_name(), color_scheme)
        self.assertIsNotNone(make_four_block_figure.get_type())
        self.assertEqual(make_four_block_figure.get_blocks_per_figure(), 4)
        self.assertIsNotNone(make_four_block_figure.get_figure_shape())

    def test_make_four_block_figure_new_figure(self):
        color_scheme = TraditionalTetrisColors()
        make_four_block_figure = MakeFourBlockFigure(2, 3, color_scheme)
        new_figure = make_four_block_figure.get_new_figure(color_scheme)

        self.assertIsInstance(new_figure, MakeFourBlockFigure)
        self.assertEqual(new_figure.get_shift_x(), 3)
        self.assertEqual(new_figure.get_shift_y(), 0)
        self.assertEqual(new_figure.get_rotation(), 0)
        self.assertIsNotNone(new_figure.get_exact_color())
        self.assertEqual(new_figure.get_color_scheme_name(), color_scheme)
        self.assertIsNotNone(new_figure.get_type())
        self.assertEqual(new_figure.get_blocks_per_figure(), 4)
        self.assertIsNotNone(new_figure.get_figure_shape())

if __name__ == '__main__':
    unittest.main()
