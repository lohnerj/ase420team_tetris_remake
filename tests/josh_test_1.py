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
        self.assertEqual(Color().get_color("PURPLE"), (120, 37, 179))
        self.assertEqual(Color().get_color("LIGHT_BLUE"), (100, 179, 179))
        self.assertEqual(Color().get_color("BROWN"), (80, 34, 22))
        self.assertEqual(Color().get_color("LIGHT_GREEN"), (80, 134, 22))
        self.assertEqual(Color().get_color("RED"), (180, 34, 22))
        self.assertEqual(Color().get_color("PINKISH_PURPLE"), (180, 34, 122))
        self.assertEqual(Color().get_color("ORANGE"), (255, 97, 3))
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