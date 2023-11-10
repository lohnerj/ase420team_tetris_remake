import random
import pygame
from tkinter import *  # for pop up box

class Color(object):
    colors = (
        (0, 0, 0),  # We don't use this
        (120, 37, 179),
        (100, 179, 179),
        (80, 34, 22),
        (80, 134, 22),
        (180, 34, 22),
        (180, 34, 122),
    )
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
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
class MakeFigure(StartingValues):
    def __init__(self, shift_x, shift_y):
        super().__init__()
        self._color = random.randint(1, len(Color.colors) - 1)
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

    def get_color(self):
        return self._color


class MakeFourBlockFigure(MakeFigure):
    figures = (
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    )

    def __init__(self, shift_x, shift_y):
        super().__init__(shift_x, shift_y)
        self._type = random.randint(0, len(self.figures) - 1)
        self._blocksPerFigure = 4

    def get_type(self):
        return self._type

    def get_blocks_per_figure(self):
        return self._blocksPerFigure

    def get_figure_shape(self):
        return self.figures[self.get_type()][self.get_rotation()]

    def get_new_figure(self):
        return MakeFourBlockFigure(3, 0)


class MakeFiveBlockFigure(MakeFigure):
    figures = (
        [[2, 7, 12, 17, 22], [5, 6, 7, 8, 9]],
        [[11, 12, 16, 17, 21], [10, 11, 12, 16, 17], [7, 11, 12, 16, 17], [11, 12, 16, 17, 18]],
        [[2, 7, 12, 17, 18], [14, 13, 12, 11, 16], [1, 2, 7, 12, 17], [11, 12, 13, 14, 9]],
        [[6, 11, 16, 17, 18], [8, 7, 6, 11, 16], [18, 13, 8, 7, 6], [16, 17, 18, 13, 8]],
        [[6, 11, 12, 13, 8], [8, 7, 12, 17, 18], [18, 13, 12, 11, 16], [16, 17, 12, 7, 6]],
        [[6, 7, 8, 12, 17], [7, 12, 17, 11, 10], [7, 12, 17, 18, 16], [7, 12, 17, 13, 14]],
        [[6, 7, 8, 9, 12], [17, 12, 7, 2, 6], [5, 6, 7, 8, 2], [2, 7, 12, 17, 13]],
    )

    def __init__(self, shift_x, shift_y):
        super().__init__(shift_x, shift_y)
        self._type = random.randint(0, len(self.figures) - 1)
        self._blocksPerFigure = 5

    def get_type(self):
        return self._type

    def get_blocks_per_figure(self):
        return self._blocksPerFigure

    def get_figure_shape(self):
        return self.figures[self.get_type()][self.get_rotation()]

    def get_new_figure(self):
        return MakeFiveBlockFigure(3, 0)

class MakeSixBlockFigure(MakeFigure):
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

    def __init__(self, shift_x, shift_y):
        super().__init__(shift_x, shift_y)
        self._type = random.randint(0, len(self.figures) - 1)
        self._blocksPerFigure = 6

    def get_type(self):
        return self._type

    def get_blocks_per_figure(self):
        return self._blocksPerFigure

    def get_figure_shape(self):
        return self.figures[self.get_type()][self.get_rotation()]

    def get_new_figure(self):
        return MakeSixBlockFigure(3, 0)


class Board(StartingValues):
    def __init__(self):
        super().__init__()
        self.play_sound = PlaySound()
        #self.play_sound = play_sound
        self._field = []
        for i in range(self.get_height()):
            new_line = [0] * self.get_width()
            self.add_to_field(new_line)
    def get_current_field(self):
        return self._field
    def add_to_field(self, new_line):
        self._field.append(new_line)
    def update_field(self, field):
        self._field = field
    def draw_board(self, screen):
        screen.fill(Color().WHITE)
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                pygame.draw.rect(screen, Color().GRAY, [self.get_startX() + self.get_blockSize() * j,
                                                        self.get_startY() + self.get_blockSize() * i,
                                                        self.get_blockSize(),
                                                        self.get_blockSize()], 1)
                if self.get_current_field()[i][j] > 0:
                    pygame.draw.rect(screen, Color().colors[self.get_current_field()[i][j]],
                                     [self.get_startX() + self.get_blockSize() * j + 1,
                                      self.get_startY() + self.get_blockSize() * i + 1,
                                      self.get_blockSize() - 2, self.get_blockSize() - 1])
    def break_lines(self):
        def check_row_filled(current_field, height, width):
            for i in range(1, height):
                zeros = 0
                for j in range(width):
                    if current_field[i][j] == 0:
                        zeros += 1
                if zeros == 0:
                    self.play_sound.play_tetris_sound()
                    #self.play_sound.play_tetris_sound()
                    delete_row(current_field, width, i)
        def delete_row(current_field, width, current_row):
            old_field = current_field
            new_field = current_field
            for k in range(current_row, 1, -1):
                for j in range(width):
                    new_field[k][j] = old_field[k - 1][j]
            return new_field
        check_row_filled(self.get_current_field(), self.get_height(), self.get_width())
class ManipulateFigure(object):
    def __init__(self, current_figure, board):
        super().__init__()
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
                    if i + self.get_current_figure().get_shift_y() > self.get_current_board().get_height() - 1 or \
                            j + self.get_current_figure().get_shift_x() > self.get_current_board().get_width() - 1 or \
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
                        j + self.get_current_figure().get_shift_x()] = self.get_current_figure().get_color()
        self.get_current_board().update_field(new_field)
        self.get_current_board().break_lines()
        #self.play_sound.play_place_sound()
        self._current_figure = self.get_current_figure().get_new_figure()
        if self.intersects():
            self.get_current_board().set_state("Gameover")
    def draw_figure(self, screen):
        for i in range(self.get_current_figure().get_blocks_per_figure()):
            for j in range(self.get_current_figure().get_blocks_per_figure()):
                p = i * self.get_current_figure().get_blocks_per_figure() + j
                if p in self.get_current_figure().get_figure_shape():
                    pygame.draw.rect(screen, Color().colors[self.get_current_figure().get_color()],
                                     [
                                         self.get_current_figure().get_startX() + self.get_current_figure().get_blockSize() *
                                         (j + self.get_current_figure().get_shift_x()) + 1,
                                         self.get_current_figure().get_startY() + self.get_current_figure().get_blockSize() *
                                         (i + self.get_current_figure().get_shift_y()) + 1,
                                         self.get_current_figure().get_blockSize() - 2,
                                         self.get_current_figure().get_blockSize() - 2])
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


class MakePopUpBox(object):
    def __init__(self):
        self._figure = 0

    def set_figure_size_selected(self, figure_size_selected):
        self._figure = figure_size_selected

    def get_figure_size_selected(self):
        return self._figure

    def get_which_figure_size_user_chooses(self):
        root = Tk()
        root.title("Pick which figures you want to play with")
        width = 400
        height = 500

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x_position = (screen_width / 2) - (width / 2)
        y_position = (screen_height / 2) - (height / 2)

        root.geometry('%dx%d+%d+%d' % (width, height, x_position, y_position))

        def four_figure_clicked():
            self.set_figure_size_selected(MakeFourBlockFigure(3, 0))
            root.destroy()

        def five_figure_clicked():
            self.set_figure_size_selected(MakeFiveBlockFigure(3, 0))
            root.destroy()

        def six_figure_clicked():
            self.set_figure_size_selected(MakeSixBlockFigure(3, 0))
            root.destroy()

        buttonFourBlockFigure = Button(root, text="4 block figures", padx=40, pady=20, command=four_figure_clicked, bg="pink")
        buttonFiveBlockFigure = Button(root, text="5 block figures", padx=40, pady=20, command=five_figure_clicked, bg="pink")
        buttonSixBlockFigure = Button(root, text="6 block figures", padx=40, pady=20, command=six_figure_clicked, bg="pink")
        label = Label(root, text="Select which figures you want to play with!", padx=30, pady=20)
        label.pack()
        buttonFourBlockFigure.pack()
        buttonFiveBlockFigure.pack()
        buttonSixBlockFigure.pack()
        root.mainloop()
        return self.get_figure_size_selected()


class Pause:
    def __init__(self, screen):
        self.font = pygame.font.Font(None, 30)
        self.font.set_bold(False)
        self.paused = False
        self.play_button_text = self.font.render(">", True, (0, 0, 0)) #\u25B6
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

    def draw(self, screen):
        screen.blit(self.current_button_text, self.current_button_rect)

class PlaySound:
    def __init__(self):
        pygame.mixer.init(44100, -16, 2, 2048)
        self.background_channel = pygame.mixer.Channel(1) 
        self.movement_channel = pygame.mixer.Channel(2) 
        self.tetris_channel = pygame.mixer.Channel(3) 
        self.quiet_sound = 0.2
        self.background_sound = pygame.mixer.Sound("util/background_sound.wav")
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
        side_sound = pygame.mixer.Sound("util/side_sound.wav")
        side_sound.set_volume(self.quiet_sound)
        self.movement_channel.play(side_sound)

    def play_rotate_sound(self):
        rotate_sound = rotate_sound = pygame.mixer.Sound("util/rotate_sound.wav")
        self.movement_channel.play(rotate_sound)
        
    def play_place_sound(self):
        place_sound = place_sound = pygame.mixer.Sound("util/place_sound.wav")
        place_sound.set_volume(self.quiet_sound)
        self.movement_channel.play(place_sound)

    def play_pause_sound(self):
        pause_sound = pygame.mixer.Sound("util/pause_sound.wav")
        self.movement_channel.play(pause_sound)

    def play_resume_sound(self):
        resume_sound = pygame.mixer.Sound("util/resume_sound.wav")
        resume_sound.set_volume(self.quiet_sound)
        self.movement_channel.play(resume_sound)

    def play_tetris_sound(self):
        tetris_sound = pygame.mixer.Sound("util/tetris_sound.wav")
        tetris_sound.set_volume(0.5)
        self.tetris_channel.play(tetris_sound)

    def play_gameover_sound(self):
        gameover_sound = pygame.mixer.Sound("util/gameover_sound.wav")
        gameover_sound.set_volume(self.quiet_sound)
        self.movement_channel.play(gameover_sound)

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.figure = MakePopUpBox().get_which_figure_size_user_chooses()
        self.board = Board()
        self.move = Move(self.figure, self.board)
        self.done = False
        self.level = 1
        self.paused = False
        self.pressing_down = False
        self.play_sound = PlaySound()

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

        self.play_sound.play_background_sound()

        while not self.done:
            counter += 1
            if counter > 100000:
                counter = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if pause_button.current_button_rect.collidepoint(event.pos):
                        self.toggle_pause()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if not self.paused:
                            self.move.rotate()
                    if event.key == pygame.K_LEFT:
                        if not self.paused:
                            self.move.go_side(-1)
                    if event.key == pygame.K_RIGHT:
                        if not self.paused:
                            self.move.go_side(1)
                    if event.key == pygame.K_DOWN:
                        self.pressing_down = True
                    if event.key == pygame.K_SPACE:
                        self.toggle_pause()
                if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    self.pressing_down = False

            if not self.paused:
                if counter % (fps // 2 // self.level) == 0 or self.pressing_down:
                    if self.board.get_state() == "Start":
                        self.move.go_down()

            self.screen.fill(Color.WHITE)

            if not self.paused:
                self.board.draw_board(self.screen)
                self.move.draw_figure(self.screen)
            else:
                pause_text = pause_button.font.render("Paused", True, Color.BLACK)
                pause_rect = pause_text.get_rect()
                pause_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
                self.screen.blit(pause_text, pause_rect)

            if self.board.get_state() == "Gameover":
                self.play_sound.play_gameover_sound()
                self.done = True

            pause_button.draw(self.screen)

            pygame.display.flip()
            clock.tick(fps)
            
    def get_user_figures_pick(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pause_button.rect.collidepoint(event.pos):
                    self.toggle_pause()

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((400, 500))

    pause_button = Pause(screen)
    game = Game(screen)
    game.run()

    pygame.quit()