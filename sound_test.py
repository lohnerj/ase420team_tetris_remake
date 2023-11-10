import unittest
import pygame
from final_tetris_refactored import PlaySound

class TestTetrisSounds(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def test_background_sound(self):
        sound_player = PlaySound()

        try:
            sound_player.play_background_sound()
        except pygame.error:
            self.fail("Background sound couldn't be played.")

    def test_stop_background_sound(self):
        sound_player = PlaySound()
        sound_player.play_background_sound()
        
        self.assertTrue(sound_player.background_channel.get_busy(), "Background sound should be playing.")

        sound_player.stop_background_sound()

        self.assertFalse(sound_player.background_channel.get_busy(), "Background sound should stop after calling stop.")


    def test_side_sound(self):
        sound_player = PlaySound()

        try:
            sound_player.play_side_sound()
        except pygame.error:
            self.fail("Side sound couldn't be played.")

    def test_rotate_sound(self):
        sound_player = PlaySound()

        try:
            sound_player.play_rotate_sound()
        except pygame.error:
            self.fail("Rotate sound couldn't be played.")

    
    def test_place_sound(self):
        sound_player = PlaySound()

        try:
            sound_player.play_place_sound()
        except pygame.error:
            self.fail("Place sound couldn't be played.")

    def test_pause_sound(self):
        sound_player = PlaySound()

        try:
            sound_player.play_pause_sound()
        except pygame.error:
            self.fail("Pause sound couldn't be played.")

    def test_resume_sound(self):
        sound_player = PlaySound()

        try:
            sound_player.play_resume_sound()
        except pygame.error:
            self.fail("Resume sound couldn't be played.")


    def test_tetris_sound(self):
        sound_player = PlaySound()

        try:
            sound_player.play_tetris_sound()
        except pygame.error:
            self.fail("Tetris sound couldn't be played.")

    def test_gameover_sound(self):
        sound_player = PlaySound()

        try:
            sound_player.play_gameover_sound()
        except pygame.error:
            self.fail("GameOver sound couldn't be played.")







    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
