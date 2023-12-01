import unittest
import pygame
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import final_tetris_refactored as ftr

class TestBackgroundColors(unittest.TestCase):

    def testThatBackgroundColorPickedFromSelectionBoxIsAValidBackgroundColorOption(self):
        all_background_color_options = ((255, 182, 193), 
                                    (135, 206, 235),
                                    (189, 252, 201),
                                    (205, 193, 197),
                                   (255, 255, 255),
                                    (0, 0, 0))
        ftr.pygame.init()
        startmenu = ftr.StartMenu()
        startmenu.display_background_color_options()
        background_color_chosen = startmenu.get_background_color()
        
        self.assertIn(background_color_chosen, all_background_color_options)
if __name__ == '__main__':
    unittest.main()
    

