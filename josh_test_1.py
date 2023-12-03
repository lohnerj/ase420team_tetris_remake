import unittest
from final_tetris_refactored import Color, StartingValues, BrightTetrisColors

from unittest.mock import patch

class Basic_Tests(unittest.TestCase):

    def setUp(self):
        self.color = Color()
        self.starting_values = StartingValues()
        self.color_scheme = BrightTetrisColors()
        

    
    #Regression
    def test_color_methods(self):
        self.assertEqual(self.color.get_purple(), (120, 37, 179))
        self.assertEqual(self.color.get_light_blue(), (100, 179, 179))
        self.assertEqual(self.color.get_brown(), (80, 34, 22))
        self.assertEqual(self.color.get_light_green(), (80, 134, 22))
        self.assertEqual(self.color.get_red(), (180, 34, 22))
        self.assertEqual(self.color.get_pinkish_purple(), (180, 34, 122))
        self.assertEqual(self.color.get_orange(), (255, 97, 3))
    #Regression
    def test_starting_values_methods(self):
        self.assertEqual(self.starting_values.get_startX(), 100)
        self.assertEqual(self.starting_values.get_startY(), 60)
        self.assertEqual(self.starting_values.get_blockSize(), 20)
        self.assertEqual(self.starting_values.get_state(), "Start")
        self.assertEqual(self.starting_values.get_height(), 20)
        self.assertEqual(self.starting_values.get_width(), 10)
    #Regression
    def test_set_state_method(self):
        self.assertEqual(self.starting_values.get_state(), "Start")
        self.starting_values.set_state("NewState")
        self.assertEqual(self.starting_values.get_state(), "NewState")
    
    

    


#Driver statement
if __name__ == '__main__':
    unittest.main()