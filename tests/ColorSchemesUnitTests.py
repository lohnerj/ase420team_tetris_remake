import unittest
import final_tetris_refactored as ftr

class TestColorSchemes(unittest.TestCase):

    def testTraditionalColors(self):
        traditional_color_scheme = ftr.TraditionalTetrisColors()
        colors = traditional_color_scheme.getColorScheme()
        self.assertEqual(colors[0], (0, 0, 0))
        self.assertEqual(colors[1], (120, 37, 179))
        self.assertEqual(colors[2], (100, 179, 179))
        self.assertEqual(colors[3], (80, 34, 22))
        self.assertEqual(colors[4], (80, 134, 22))
        self.assertEqual(colors[5], (180, 34, 22))
        self.assertEqual(colors[6], (180, 34, 122))

    def testRainbowColors(self):
        rainbow_color_scheme = ftr.RainbowTetrisColors()
        colors = rainbow_color_scheme.getColorScheme()
        self.assertEqual(colors[0], (0, 0, 0))
        self.assertEqual(colors[1], (180, 34, 22))
        self.assertEqual(colors[2], (255, 97, 3))
        self.assertEqual(colors[3], (255, 255, 0))
        self.assertEqual(colors[4], (0,128,0))
        self.assertEqual(colors[5], (0, 0, 255))
        self.assertEqual(colors[6], (120, 37, 179))

    def testAutumnColors(self):
        autumn_color_scheme = ftr.AutumnTetrisColors()
        colors = autumn_color_scheme.getColorScheme()
        self.assertEqual(colors[0], (0, 0, 0))
        self.assertEqual(colors[1], (205, 55, 0))
        self.assertEqual(colors[2], (128, 0, 0))
        self.assertEqual(colors[3], (205, 173, 0))
        self.assertEqual(colors[4], (138, 54, 15))
        self.assertEqual(colors[5], (107, 142, 35))
        self.assertEqual(colors[6], (94, 38, 18))

    def testBrightColors(self):
        bright_color_scheme = ftr.BrightTetrisColors()
        colors = bright_color_scheme.getColorScheme()
        self.assertEqual(colors[0], (0, 0, 0))
        self.assertEqual(colors[1], (57, 255, 20))
        self.assertEqual(colors[2], (255,105,180))
        self.assertEqual(colors[3], (31, 81, 255))
        self.assertEqual(colors[4], (255, 95, 31))
        self.assertEqual(colors[5], (224,231,34)) #make sure that i fixed the issue of neon yellow returning neon orange!!
        self.assertEqual(colors[6], (0,245,255))


if __name__ == '__main__':
    unittest.main()