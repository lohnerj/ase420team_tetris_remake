import unittest
import pygame
from final_tetris_refactored import Pause

class TestPause(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def test_pause_toggle(self):
        screen = pygame.display.set_mode((400, 500))
        pause_button = Pause(screen)

        # Initially, the game should not be paused
        self.assertFalse(pause_button.is_paused(), "Game is already paused.")

        # Toggle the pause
        pause_button.toggle()
        self.assertTrue(pause_button.is_paused(), "Pause toggle not working.")

        # Toggle again to resume
        pause_button.toggle()
        self.assertFalse(pause_button.is_paused(), "Pause toggle not working to resume.")

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
