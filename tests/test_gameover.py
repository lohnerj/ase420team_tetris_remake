import unittest
from unittest.mock import patch
import pygame

from final_tetris_refactored import Gameover

class TestGameover(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.Surface((800, 600))  # Create a surface for testing
        self.gameover = Gameover(self.screen)

    def tearDown(self):
        pygame.quit()

    def test_handle_events_restart(self):
        with patch('pygame.event.get', return_value=[pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_r})]):
            result = self.gameover.handle_events()
        self.assertEqual(result, "restart")

    def test_handle_events_quit(self):
        with patch('pygame.event.get', return_value=[pygame.event.Event(pygame.QUIT)]):
            result = self.gameover.handle_events()
        self.assertEqual(result, "quit")

    def test_handle_events_no_event(self):
        with patch('pygame.event.get', return_value=[]):
            result = self.gameover.handle_events()
        self.assertIsNone(result)

    def test_draw(self):
        with patch.object(self.gameover, 'draw') as mock_draw:
            self.gameover.draw(self.screen)
        mock_draw.assert_called_once_with(self.screen)

if __name__ == '__main__':
    unittest.main()