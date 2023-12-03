import random
import pygame
from abc import ABCMeta, abstractmethod

class Color(object):
    def __init__(self):
        self._colors = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "GRAY": (128, 128, 128),
        "PURPLE": (120, 37, 179),
        "LIGHT_BLUE": (100, 179, 179),
        "BROWN": (80, 34, 22),
        "LIGHT_GREEN": (80, 134, 22),
        "RED": (180, 34, 22),
        "PINKISH_PURPLE": (180, 34, 122),
        "ORANGE": (255, 97, 3),
        "YELLOW": (255, 255, 0),
        "GREEN": (0,128,0),
        "BLUE": (0, 0, 255), 
        "RUST_ORANGE": (205, 55, 0),
        "MAROON": (128, 0, 0),
        "GOLDEN_YELLOW": (205, 173, 0),
        "BURNT_SIENNA": (138, 54, 15),
        "OLIVE_GREEN": (107, 142, 35),
        "DARK_BROWN": (94, 38, 18),
        "LIGHT_PINK": (255, 182, 193),
        "SKY_BLUE": (135, 206, 235),
        "MINT": (189, 252, 201),
        "LAVENDER": (205, 193, 197),
        "PALE_TURQUOISE": (102, 139, 139),
        "PALE_GOLDENROD": (238, 232, 170),
        "NEON_GREEN": (57, 255, 20),
        "HOT_PINK": (255,105,180),
        "NEON_BLUE": (31, 81, 255),
        "NEON_ORANGE": (255, 95, 31),
        "NEON_YELLOW": ((224,231,34)),
        "TURQOISE": (0,245,255),
        }

    def get_color(self, name):
        return self._colors.get(name)


class ColorScheme(metaclass=ABCMeta):
    @abstractmethod
    def get_colors(self): pass
       

class TraditionalTetrisColors(ColorScheme):
    def __init__(self):
        self._colors = (Color().get_color("BLACK"),
                        Color().get_color("PURPLE"), 
                        Color().get_color("LIGHT_BLUE"),
                        Color().get_color("BROWN"),
                        Color().get_color("LIGHT_GREEN"),
                        Color().get_color("RED"),
                        Color().get_color("PINKISH_PURPLE"))
    def get_colors(self):
        return self._colors
    
class RainbowTetrisColors(ColorScheme):
    def __init__(self):
        self._colors = (Color().get_color("BLACK"),
                        Color().get_color("RED"),
                        Color().get_color("ORANGE"),
                        Color().get_color("YELLOW"),
                        Color().get_color("GREEN"),
                        Color().get_color("BLUE"),
                        Color().get_color("PURPLE"))
    def get_colors(self):
        return self._colors
    
class AutumnTetrisColors(ColorScheme):
    def __init__(self):
        self._colors = (Color().get_color("BLACK"),
                        Color().get_color("RUST_ORANGE"),
                        Color().get_color("MAROON"),
                        Color().get_color("GOLDEN_YELLOW),
                        Color().get_color("BURNT_SIENNA"),
                        Color().get_color("OLIVE_GREEN"),
                        Color().get_color("DARK_BROWN"))
    def get_colors(self):
        return self._colors
    
class BrightTetrisColors(ColorScheme):
    def __init__(self):
        self._colors = (Color().get_color("BLACK"),
                        Color().get_color("NEON_GREEN"),
                        Color().get_color("HOT_PINK"),
                        Color().get_color("NEON_BLUE"),
                        Color().get_color("NEON_ORANGE"),
                        Color().get_color("NEON_YELLOW"),
                        Color().get_color("TURQOISE"))
    def get_colors(self):
        return self._colors


class StartingValues(object):
    def __init__(self):
        self._startX = 100
        self._startY = 60
        self._blockSize = 20
        self._height = 20
        self._width = 10
        self._state = "Start"
    def get_startX(self):
        return self._startX
    def get_startY(self):
        return self._startY
    def get_blockSize(self):
        return self._blockSize
    def get_state(self):
        return self._state
    def get_height(self):
        return self._height
    def get_width(self):
        return self._width
    def set_state(self, state):
        self._state = state


class BaseFigure(object):
    def __init__(self, shift_x, shift_y, color_scheme):
        self._exact_color = random.randint(1, len(color_scheme.get_colors()) - 1) #!!
        self._color_scheme = color_scheme
        self._rotation = 0
        self._shift_x = shift_x
        self._shift_y = shift_y

    def get_shift_x(self):
        return self._shift_x

    def get_shift_y(self):
        return self._shift_y

    def update_shift_x(self, shift_x):
        self._shift_x = shift_x

    def update_shift_y(self, shift_y):
        self._shift_y = shift_y

    def update_rotation(self, rotation):
        self._rotation = rotation

    def get_rotation(self):
        return self._rotation

    def get_exact_color(self):
        return self._exact_color
        
    def get_color_scheme_name(self): #!!!
        return self._color_scheme


class MakeFourBlockFigure(BaseFigure):
    figures = (
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    )

    def __init__(self, shift_x, shift_y, color_scheme):
        super().__init__(shift_x, shift_y, color_scheme)
        self._type = random.randint(0, len(self.figures) - 1)
        self._BLOCKS_PER_FIGURE = 4

    def get_type(self):
        return self._type

    def get_blocks_per_figure(self):
        return self._BLOCKS_PER_FIGURE

    def get_figure_shape(self):
        return self.figures[self.get_type()][self.get_rotation()]

    def get_new_figure(self, color_scheme):
        return MakeFourBlockFigure(3, 0, color_scheme) #!!!


class MakeFiveBlockFigure(BaseFigure):
    figures = (
        [[2, 7, 12, 17, 22], [5, 6, 7, 8, 9]],
        [[11, 12, 16, 17, 21], [10, 11, 12, 16, 17], [7, 11, 12, 16, 17], [11, 12, 16, 17, 18]],
        [[2, 7, 12, 17, 18], [14, 13, 12, 11, 16], [1, 2, 7, 12, 17], [11, 12, 13, 14, 9]],
        [[6, 11, 16, 17, 18], [8, 7, 6, 11, 16], [18, 13, 8, 7, 6], [16, 17, 18, 13, 8]],
        [[6, 11, 12, 13, 8], [8, 7, 12, 17, 18], [18, 13, 12, 11, 16], [16, 17, 12, 7, 6]],
        [[6, 7, 8, 12, 17], [7, 12, 17, 11, 10], [7, 12, 17, 18, 16], [7, 12, 17, 13, 14]],
        [[6, 7, 8, 9, 12], [17, 12, 7, 2, 6], [5, 6, 7, 8, 2], [2, 7, 12, 17, 13]],
    )

    def __init__(self, shift_x, shift_y, color_scheme):
        super().__init__(shift_x, shift_y, color_scheme)
        self._type = random.randint(0, len(self.figures) - 1)
        self._BLOCKS_PER_FIGURE = 5

    def get_type(self):
        return self._type

    def get_blocks_per_figure(self):
        return self._BLOCKS_PER_FIGURE

    def get_figure_shape(self):
        return self.figures[self.get_type()][self.get_rotation()]

    def get_new_figure(self, color_scheme):
        return MakeFiveBlockFigure(3, 0, color_scheme)

class MakeSixBlockFigure(BaseFigure):
    figures = (
        [[12,13,14,15,16,17], [2,8,14,20,26,32]],
        [[13,19,20,21,15,9], [15,14,20,26,27,28], [22,16,15,14,20,26],[26,27,21,15,14,13]],
        [[8,14,20,9,15,21], [16,15,14,22,21,20]],
        [[6,7,8,9,10,14], [3,9,15,21,27,14], [18,19,20,21,22,14], [1,7,13,19,25,14]],
        [[12,13,14,15,21,27], [3,9,15,21,20,19], [23,22,21,20,14,8], [32,26,20,14,15,16]],
        [[13,14,15,16,17,23], [9,15,21,27,33,32], [23,22,21,20,19,13], [27,21,15,9,3,4]],
        [[7,8,14,20,21,22], [9,15,14,13,19,25], [21,20,14,8,7,6], [19,13,14,15,9,3]],
        [[7,8,9,14,20,26], [9,15,21,14,13,12], [21,20,19,14,8,2], [19,13,7,14,15,16]],
        [[14,15,20,21,22,23], [14,15,20,21,26,32], [14,15,20,21,13,12], [14,15,20,21,9,3]],
        [[9,15,21,27,14,16], [13,14,15,16,9,21], [9,15,21,27,20,22], [14,15,16,17,9,21]],
        [[13,14,15,16,21,27], [9,15,21,27,20,19], [23,22,21,20,15,9], [27,21,15,9,16,17]],
    )

    def __init__(self, shift_x, shift_y, color_scheme):
        super().__init__(shift_x, shift_y, color_scheme)
        self._type = random.randint(0, len(self.figures) - 1)
        self._BLOCKS_PER_FIGURE = 6

    def get_type(self):
        return self._type

    def get_blocks_per_figure(self):
        return self._BLOCKS_PER_FIGURE

    def get_figure_shape(self):
        return self.figures[self.get_type()][self.get_rotation()]

    def get_new_figure(self, color_scheme):
        return MakeSixBlockFigure(3, 0, color_scheme)
    

class FactoryClassInterface(metaclass=ABCMeta):
    @abstractmethod
    def create_figure(self, color_scheme): pass

class FactoryClass(object):
    def create_figure(self, color_scheme, number_of_blocks_in_figure):
        if number_of_blocks_in_figure == 4:
            return FourBlockFigureFactory().create_figure(color_scheme)
        elif number_of_blocks_in_figure == 5:
            return FiveBlockFigureFactory().create_figure(color_scheme)
        elif number_of_blocks_in_figure == 6:
            return SixBlockFigureFactory().create_figure(color_scheme)
        else:
            return None
        
        
class FourBlockFigureFactory(FactoryClassInterface):
    def create_figure(self, color_scheme):
        return MakeFourBlockFigure(3, 0, color_scheme)
    
class FiveBlockFigureFactory(FactoryClassInterface):
    def create_figure(self, color_scheme):
        return MakeFiveBlockFigure(3, 0, color_scheme)

class SixBlockFigureFactory(FactoryClassInterface):
    def create_figure(self, color_scheme):
        return MakeSixBlockFigure(3, 0, color_scheme)


class Board(object):
    def __init__(self, color_scheme):
        self.play_sound = PlaySound()
        self._starting_values = StartingValues()
        self._field = []
        self._color_scheme = color_scheme.get_colors()
        for i in range(self._starting_values.get_height()):
            new_line = [0] * self._starting_values.get_width()
            self.add_to_field(new_line)
    def get_starting_values(self):
        return self._starting_values
    def get_current_field(self):
        return self._field
    def add_to_field(self, new_line):
        self._field.append(new_line)
    def update_field(self, field):
        self._field = field
    def draw_board(self, screen, color):
        screen.fill(color)
        for i in range(self._starting_values.get_height()):
            for j in range(self._starting_values.get_width()):
                pygame.draw.rect(screen, Color().get_color("GRAY"), [self._starting_values.get_startX() + self._starting_values.get_blockSize() * j,
                                                        self._starting_values.get_startY() + self._starting_values.get_blockSize() * i,
                                                        self._starting_values.get_blockSize(),
                                                        self._starting_values.get_blockSize()], 1)
                if self.get_current_field()[i][j] > 0:
                    pygame.draw.rect(screen, self._color_scheme[self.get_current_field()[i][j]],
                                     [self._starting_values.get_startX() + self._starting_values.get_blockSize() * j + 1,
                                      self._starting_values.get_startY() + self._starting_values.get_blockSize() * i + 1,
                                      self._starting_values.get_blockSize() - 2, self._starting_values.get_blockSize() - 1])
    def break_lines(self):
        def check_row_filled(current_field, height, width):
            for i in range(1, height):
                zeros = 0
                for j in range(width):
                    if current_field[i][j] == 0:
                        zeros += 1
                if zeros == 0:
                    self.play_sound.play_tetris_sound()
                    delete_row(current_field, width, i)
        def delete_row(current_field, width, current_row):
            old_field = current_field
            new_field = current_field
            for k in range(current_row, 1, -1):
                for j in range(width):
                    new_field[k][j] = old_field[k - 1][j]
            return new_field
        check_row_filled(self.get_current_field(), self._starting_values.get_height(), self._starting_values.get_width())


class ManipulateFigure(object):
    def __init__(self, current_figure, board):
        #super().__init__()
        self._current_figure = current_figure
        self._board = board
    def get_current_figure(self):
        return self._current_figure
    def get_current_board(self):
        return self._board
    def intersects(self):
        intersection = False
        for i in range(self.get_current_figure().get_blocks_per_figure()):
            for j in range(self.get_current_figure().get_blocks_per_figure()):
                if i * self.get_current_figure().get_blocks_per_figure() + j in self.get_current_figure().get_figure_shape():
                    if i + self.get_current_figure().get_shift_y() > self.get_current_board().get_starting_values().get_height() - 1 or \
                            j + self.get_current_figure().get_shift_x() > self.get_current_board().get_starting_values().get_width() - 1 or \
                            j + self.get_current_figure().get_shift_x() < 0 or \
                            self.get_current_board().get_current_field()[
                                i + self.get_current_figure().get_shift_y()][
                                j + self.get_current_figure().get_shift_x()] > 0:
                        intersection = True
        return intersection
    def rotate(self):
        old_rotation = self.get_current_figure().get_rotation()
        self.get_current_figure().update_rotation(
            (self.get_current_figure().get_rotation() + 1)
            % len(
                self.get_current_figure().figures[self.get_current_figure().get_type()]))
        if not self.intersects():
            self.play_sound.play_rotate_sound()
        else:
            self.get_current_figure().update_rotation(old_rotation)
    def freeze(self):
        self.play_sound.play_place_sound()
        new_field = self.get_current_board().get_current_field()
        for i in range(self.get_current_figure().get_blocks_per_figure()):
            for j in range(self.get_current_figure().get_blocks_per_figure()):
                if i * self.get_current_figure().get_blocks_per_figure() + j in self.get_current_figure().get_figure_shape():
                    new_field[i + self.get_current_figure().get_shift_y()][
                        j + self.get_current_figure().get_shift_x()] = self.get_current_figure().get_exact_color()
        self.get_current_board().update_field(new_field)
        self.get_current_board().break_lines()
        self._current_figure = FactoryClass().create_figure(self.get_current_figure().get_color_scheme_name(), self.get_current_figure().get_blocks_per_figure()) 
        if self.intersects():
            self.get_current_board().get_starting_values().set_state("Gameover")
    def draw_figure(self, screen):
        for i in range(self.get_current_figure().get_blocks_per_figure()):
            for j in range(self.get_current_figure().get_blocks_per_figure()):
                p = i * self.get_current_figure().get_blocks_per_figure() + j
                if p in self.get_current_figure().get_figure_shape():
                    pygame.draw.rect(screen, self.get_current_figure().get_color_scheme_name().get_colors()[self.get_current_figure().get_exact_color()],
                                     [
                                         self.get_current_board().get_starting_values().get_startX() + self.get_current_board().get_starting_values().get_blockSize() *
                                         (j + self.get_current_figure().get_shift_x()) + 1,
                                         self.get_current_board().get_starting_values().get_startY() +  self.get_current_board().get_starting_values().get_blockSize() *
                                         (i + self.get_current_figure().get_shift_y()) + 1,
                                          self.get_current_board().get_starting_values().get_blockSize() - 2,
                                          self.get_current_board().get_starting_values().get_blockSize() - 2])
class Move(ManipulateFigure):
    def __init__(self, current_figure, board):
        super().__init__(current_figure, board)
        self.play_sound = PlaySound()
    def go_space(self):
        while not self.intersects():
            self.get_current_figure().update_shift_y(self.get_current_figure().get_shift_y() + 1)
        self.get_current_figure().update_shift_y(self.get_current_figure().get_shift_y() - 1)
        self.freeze()
    def go_down(self):
        self.get_current_figure().update_shift_y(
            self.get_current_figure().get_shift_y() + 1)
        if self.intersects():
            self.get_current_figure().update_shift_y(self.get_current_figure().get_shift_y() - 1)
            self.freeze()
    def go_side(self, dx):
        old_x = self.get_current_figure().get_shift_x()
        self.get_current_figure().update_shift_x(self.get_current_figure().get_shift_x() + dx)
        if self.intersects():
            self.get_current_figure().update_shift_x(old_x)
        else:
            self.play_sound.play_side_sound()


class Pause:
    def __init__(self, screen):
        self.font = pygame.font.Font('util/fonts/seguisym.ttf', 25)
        self.font.set_bold(False)
        self.paused = False
        self.play_button_text = self.font.render("\u25B6", True, (0, 0, 0))
        self.play_button_rect = self.play_button_text.get_rect()
        self.play_button_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        self.pause_button_text = self.font.render("||", True, (0, 0, 0))
        self.pause_button_rect = self.pause_button_text.get_rect()
        self.pause_button_rect.x = (screen.get_width() - self.pause_button_rect.width) - 20
        self.pause_button_rect.y = 15
        self.current_button_text = self.pause_button_text
        self.current_button_rect = self.pause_button_rect
        self.play_sound = PlaySound()

    def toggle(self):
        self.paused = not self.paused
        if self.paused:
            self.play_sound.play_pause_sound()
            self.current_button_text = self.play_button_text
        else:
            self.play_sound.play_resume_sound()
            self.current_button_text = self.pause_button_text

    def is_paused(self):
        return self.paused
    
    def pausedraw(self, screen):
        screen.blit(self.current_button_text, self.current_button_rect)
    
class StartMenu(object):
    def __init__(self):
        self.width = 400
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.users_selected_color_scheme = 0
        self.users_selected_figures = 0
        self.background_color = 0
        self.font = pygame.font.Font('freesansbold.ttf', 26) #should i change font to the font in the util folder?

    def set_users_choice_color_scheme(self, color_scheme_selected):
        self.users_selected_color_scheme = color_scheme_selected
    def get_users_choice_color_scheme(self):
        return self.users_selected_color_scheme
    def set_users_choice_figures(self, figure_choice):
        self.users_selected_figures = figure_choice
    def get_users_choice_figures(self):
        return self.users_selected_figures
    def set_background_color(self, background_color):
        self.background_color = background_color
    def get_background_color(self):
        return self.background_color
    
    def display_options(self, buttons, title, function_setter, function_getter, screen):
        text = self.font.render(title, True, Color().get_color("BLACK"))
        textRect = text.get_rect(topleft=(60,200))

        run = True
        while run:
            screen.fill((202,228,241))
            screen.blit(text, textRect)

            for button in buttons:
                if button.draw(screen):
                    function_setter(button.get_method_to_set_to()) #maybe rename this?
                    run = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

            pygame.display.flip()
            
        pygame.display.update()
        return function_getter()

    def display_color_schemes(self):
        
        buttons = [
            Button(10, 10, "button_images/button_classic-colors.png", .7, TraditionalTetrisColors()),
            Button(10, 75, "button_images/button_rainbow-colors.png", .7, RainbowTetrisColors()),
            Button(200, 10, "button_images/button_autumn-colors.png", .7, AutumnTetrisColors()),
            Button(215, 75, "button_images/button_bright-colors.png", .7, BrightTetrisColors())
        ]
        return self.display_options(buttons, 'Pick A Color Scheme', self.set_users_choice_color_scheme, self.get_users_choice_color_scheme, self.screen)

        
    def display_figure_selection(self):

        self.display_color_schemes()
        buttons = [
            Button(100, 250, "button_images/button_4_block-figures.png", .8, FactoryClass().create_figure(self.get_users_choice_color_scheme(), 4)),
            Button(100, 325, "button_images/button_5_block-figures.png", .8, FactoryClass().create_figure(self.get_users_choice_color_scheme(), 5)),
            Button(100, 400, "button_images/button_6_block-figures.png", .8, FactoryClass().create_figure(self.get_users_choice_color_scheme(), 6)),
        ]
        return self.display_options(buttons, 'Which Tetromino Figures?', self.set_users_choice_figures, self.get_users_choice_figures, self.screen)
    
    def display_background_color_options(self):
        
        buttons = [
            Button(10, 0, "button_images/button_light-pink.png", .8, Color().get_color("LIGHT_PINK")),
            Button(10, 65, "button_images/button_sky-blue.png", .8, Color().get_color("SKY_BLUE")),
            Button(10, 140, "button_images/button_mint.png", .8, Color().get_color("MINT")),
            Button(200, 0, "button_images/button_lavender.png", .8, Color().get_color("LAVENDER")),
            Button(200, 65, "button_images/button_white.png", .8, Color().get_color("WHITE")),
            Button(200, 140, "button_images/button_black.png", .8, Color().get_color("BLACK"))
        ]
        return self.display_options(buttons, 'Pick A Background Color', self.set_background_color, self.get_background_color, self.screen)
    

class Button(object):
    def __init__(self, x, y, image_url, scale, set_to_method):
        self.image = pygame.image.load(image_url).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.set_to = set_to_method

    def get_method_to_set_to(self):
        return self.set_to

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            
        screen.blit(self.image, self.rect)
        return action    
    

class PlaySound:
    def __init__(self):
        pygame.mixer.init(44100, -16, 2, 2048)
        self.background_channel = pygame.mixer.Channel(1) 
        self.movement_channel = pygame.mixer.Channel(2) 
        self.tetris_channel = pygame.mixer.Channel(3) 
        self.quiet_sound = 0.2
        self.background_sound = pygame.mixer.Sound("util/sounds/background_sound.wav")
        self.background_playing = False
        

    def play_background_sound(self):
        if not self.background_playing:
            self.background_sound.set_volume(0.5)
            self.background_channel.play(self.background_sound, loops=-1)
            self.background_playing = True

    def stop_background_sound(self):
        if self.background_playing:
            self.background_channel.stop()
            self.background_playing = False

    def play_side_sound(self):
        side_sound = pygame.mixer.Sound("util/sounds/side_sound.wav")
        side_sound.set_volume(self.quiet_sound)
        self.movement_channel.play(side_sound)

    def play_rotate_sound(self):
        rotate_sound = rotate_sound = pygame.mixer.Sound("util/sounds/rotate_sound.wav")
        self.movement_channel.play(rotate_sound)
        
    def play_place_sound(self):
        place_sound = place_sound = pygame.mixer.Sound("util/sounds/place_sound.wav")
        place_sound.set_volume(self.quiet_sound)
        self.movement_channel.play(place_sound)

    def play_pause_sound(self):
        pause_sound = pygame.mixer.Sound("util/sounds/pause_sound.wav")
        self.movement_channel.play(pause_sound)

    def play_resume_sound(self):
        resume_sound = pygame.mixer.Sound("util/sounds/resume_sound.wav")
        resume_sound.set_volume(self.quiet_sound)
        self.movement_channel.play(resume_sound)

    def play_tetris_sound(self):
        tetris_sound = pygame.mixer.Sound("util/sounds/tetris_sound.wav")
        tetris_sound.set_volume(0.5)
        self.tetris_channel.play(tetris_sound)

    def play_settings_sound(self):
        settings_sound = pygame.mixer.Sound("util/sounds/settings_sound.wav")
        self.movement_channel.play(settings_sound)

    def play_gameover_sound(self):
        gameover_sound = pygame.mixer.Sound("util/sounds/gameover_sound.wav")
        gameover_sound.set_volume(self.quiet_sound)
        self.movement_channel.play(gameover_sound)

class Gameover:
    def __init__(self, screen):
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Game Over", True, (255, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        self.restart_text = self.font.render("Press R to Restart", True, (0, 0, 0))
        self.restart_rect = self.restart_text.get_rect()
        self.restart_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)

    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.restart_text, self.restart_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                elif event.key == pygame.K_ESCAPE:
                    return "quit"
        return None


class Game:
    def __init__(self, screen):
        startmenu = StartMenu()
        self.screen = screen
        self.figure = startmenu.display_figure_selection()
        self.board = Board(startmenu.get_users_choice_color_scheme())
        self.move = Move(self.figure, self.board)
        self.done = False
        self.level = 1
        self.paused = False
        self.pressing_down = False
        self.play_sound = PlaySound()
        self.game_over = False
        self.game_over_screen = Gameover(screen)
        self.background_color = startmenu.display_background_color_options()

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.play_sound.stop_background_sound()
        else:
            self.play_sound.play_background_sound()
        pause_button.toggle()

    def run(self):
        fps = 25
        counter = 0
        self.game_over = False

        self.play_sound.play_background_sound()
        

        while not self.done:
            counter += 1
            if counter > 100000:
                counter = 0

            context = Context(self)
            for event in pygame.event.get():
                
                context.make_decision(event)

            if not self.paused:
                if counter % (fps // 2 // self.level) == 0 or self.pressing_down:
                    if self.board.get_starting_values().get_state() == "Start":
                        self.move.go_down()

            self.screen.fill(Color().get_color("WHITE"))

            if not self.paused:
                self.board.draw_board(self.screen, self.background_color)
                self.move.draw_figure(self.screen)
            else:
                pause_text = pause_button.font.render("Paused", True, Color().get_color("BLACK"))
                pause_rect = pause_text.get_rect()
                pause_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
                self.screen.blit(pause_text, pause_rect)

            if self.board.get_starting_values().get_state() == "Gameover":
                self.play_sound.play_gameover_sound()
                self.game_over = True
                self.display_game_over()

            pause_button.pausedraw(self.screen)

            pygame.display.flip()
            clock.tick(fps)
            

    def display_game_over(self):
        while self.game_over:
            result = self.game_over_screen.handle_events()
            if result == "restart":
                self.reset_game()
                self.game_over = False
            elif result == "quit":
                self.done = True
                self.game_over = False

            self.game_over_screen.draw(self.screen)
            pygame.display.flip()
            clock.tick(30)

    def reset_game(self):
        startmenu = StartMenu()
        self.figure = startmenu.display_figure_selection() #added
        self.board = Board(startmenu.get_users_choice_color_scheme()) #added
        self.move = Move(self.figure, self.board)
        self.level = 1
        self.paused = False
        self.pressing_down = False
        self.game_over = False
        self.background_color = startmenu.display_background_color_options() #added
        self.play_sound.play_background_sound()


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self): pass

class QuitStrategy(Strategy):
    def execute(self, game):
        game.done = True
class PauseStrategy(Strategy):
    def execute(self, game):
        game.toggle_pause()
class RotateStrategy(Strategy):
    def execute(self, game):
        game.move.rotate()
class GoLeftStrategy(Strategy):
    def execute(self, game):
        game.move.go_side(-1)
class GoRightStrategy(Strategy):
    def execute(self, game):
        game.move.go_side(1)
class GoDownStrategy(Strategy):
    def execute(self, game):
        game.pressing_down = True
class ReleaseGoDownStrategy(Strategy):
    def execute(self, game):
        game.pressing_down = False

class Context(object):
    def __init__(self, game):
        self.game = game
        self.strategy = None
    def set_strategy(self, strategy):
        self.strategy = strategy
    def make_decision(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pause_button.current_button_rect.collidepoint(event.pos):
                self.set_strategy(PauseStrategy())
        if event.type == pygame.QUIT:
            self.set_strategy(QuitStrategy())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not self.game.paused:
                    self.set_strategy(RotateStrategy())
            if event.key == pygame.K_LEFT:
                if not self.game.paused:
                    self.set_strategy(GoLeftStrategy())
            if event.key == pygame.K_RIGHT:
                if not self.game.paused:
                    self.set_strategy(GoRightStrategy())
            if event.key == pygame.K_DOWN:
                self.set_strategy(GoDownStrategy())
            if event.key == pygame.K_SPACE:
                self.set_strategy(PauseStrategy())
                self.strategy.execute(self.game)  #if strategy isn't  executed in this if statement. It will not pause the screen. There is some kind of odd timing issue that prevents that, hence why i have the execute method in this if statement.
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            self.set_strategy(ReleaseGoDownStrategy())

        if self.strategy:
            self.strategy.execute(self.game)

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((400, 500))

    pause_button = Pause(screen)
    game = Game(screen)
    game.run()

    pygame.quit()
