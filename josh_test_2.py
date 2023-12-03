import unittest
from final_tetris_refactored import Board, Color, Gameover, StartingValues, BaseFigure, BrightTetrisColors, MakeFourBlockFigure, Pause, PlaySound, Button
import pygame
import io
from unittest.mock import MagicMock, patch

class TestGameIntegration(unittest.TestCase):

    def setUp(self):
        self.starting_values = StartingValues()
        self.color_scheme = BrightTetrisColors()
        pygame.init()

    def tearDown(self):
        pygame.quit()

    

    def test_board_methods(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            board = Board(self.color_scheme)
            self.assertIsInstance(board, Board)

            # Test initial field state
            self.assertEqual(board.get_current_field(), [[0] * self.starting_values.get_width()] * self.starting_values.get_height())

            # Test drawing on the board
            screen = pygame.display.set_mode((500, 500))
            board.draw_board(screen, Color().get_color("BLACK"))
            pygame.display.flip()

    def test_pause_methods(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch.object(PlaySound, 'play_pause_sound') as mock_play_pause_sound:
                screen = pygame.display.set_mode((500, 500))
                pause = Pause(screen)

                self.assertIsInstance(pause, Pause)

                # Test initial state
                self.assertFalse(pause.is_paused())
                self.assertEqual(pause.current_button_text, pause.pause_button_text)

                # Test toggling
                initial_paused_state = pause.is_paused()
                pause.toggle()
                self.assertNotEqual(initial_paused_state, pause.is_paused())
                self.assertNotEqual(pause.current_button_text, pause.pause_button_text)
                mock_play_pause_sound.assert_called_once()  
                print(mock_stdout.getvalue())

    def test_button_methods(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            image = pygame.Surface((50, 30)) 
            button = Button(100, 100, image, 2)
            self.assertIsInstance(button, Button)

            # Test initial state
            self.assertFalse(button.clicked)

    def test_gameover_methods(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            # Create a mock for pygame.Surface
            mock_surface = MagicMock(spec=pygame.Surface)

            # Create a mock for the screen and set its return value to the mock_surface
            mock_screen = MagicMock()
            mock_screen.return_value = mock_surface

            # Initialize Gameover instance
            gameover = Gameover(mock_screen)

            # Test draw method
            with patch('pygame.Surface', mock_surface): 
                with patch.object(mock_surface(), 'fill') as mock_fill, \
                     patch.object(mock_surface(), 'blit') as mock_blit:
                    gameover.draw(mock_screen)
                    

            # Test handle_events method
            with patch.object(pygame.event, 'get', return_value=[]):
                result = gameover.handle_events()
                self.assertIsNone(result)

            with patch.object(pygame.event, 'get', return_value=[pygame.event.Event(pygame.QUIT)]):
                result = gameover.handle_events()
                self.assertEqual(result, "quit")

            with patch.object(pygame.event, 'get', return_value=[pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r)]):
                result = gameover.handle_events()
                self.assertEqual(result, "restart")

            with patch.object(pygame.event, 'get', return_value=[pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)]):
                result = gameover.handle_events()
                self.assertEqual(result, "quit")

               


#Driver statement
if __name__ == '__main__':
    unittest.main()