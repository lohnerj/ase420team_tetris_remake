# Name: Julianna Truitt
# Class: ASE 420
# Description: Refactoring tetris_ver1.py.
import random
import pygame


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
        super().__init__()
        self._type = random.randint(0, len(self.figures) - 1)
        self._color = random.randint(1, len(Color.colors) - 1)
        self._rotation = 0
        self._blocksPerFigure = 4
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

    def get_type(self):
        return self._type

    def get_color(self):
        return self._color

    def get_blocks_per_figure(self):
        return self._blocksPerFigure

    def get_figure_shape(self):
        return self.figures[self.get_type()][self.get_rotation()]


class Board(StartingValues):
    def __init__(self):
        super().__init__()
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
        if self.intersects():
            self.get_current_figure().update_rotation(old_rotation)

    def freeze(self):
        new_field = self.get_current_board().get_current_field()
        for i in range(self.get_current_figure().get_blocks_per_figure()):
            for j in range(self.get_current_figure().get_blocks_per_figure()):
                if i * self.get_current_figure().get_blocks_per_figure() + j in self.get_current_figure().get_figure_shape():
                    new_field[i + self.get_current_figure().get_shift_y()][
                        j + self.get_current_figure().get_shift_x()] = self.get_current_figure().get_color()
        self.get_current_board().update_field(new_field)
        self.get_current_board().break_lines()
        self._current_figure = MakeFigure(3, 0)
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

class Pause:
    def __init__(self, screen):
        self.font = pygame.font.Font(None, 30)
        self.font.set_bold(True)
        self.paused = False
        self.play_button_text = self.font.render(">", True, (0, 0, 0))
        self.play_button_rect = self.play_button_text.get_rect()
        self.play_button_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        self.pause_button_text = self.font.render("||", True, (0, 0, 0))
        self.pause_button_rect = self.pause_button_text.get_rect()
        self.pause_button_rect.x = (screen.get_width() - self.pause_button_rect.width) - 20
        self.pause_button_rect.y = 15
        self.current_button_text = self.pause_button_text
        self.current_button_rect = self.pause_button_rect

    def toggle(self):
        self.paused = not self.paused
        if self.paused:
            self.current_button_text = self.play_button_text
        else:
            self.current_button_text = self.pause_button_text

    def is_paused(self):
        return self.paused

    def draw(self, screen):
        screen.blit(self.current_button_text, self.current_button_rect)


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.figure = MakeFigure(3, 0)
        self.board = Board()
        self.move = Move(self.figure, self.board)
        self.done = False
        self.level = 1
        self.paused = False
        self.pressing_down = False

    def toggle_pause(self):
        self.paused = not self.paused
        pause_button.toggle()

    def run(self):
        fps = 25
        counter = 0

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
                self.done = True

            pause_button.draw(self.screen)

            pygame.display.flip()
            clock.tick(fps)

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((400, 500))

    pause_button = Pause(screen)
    game = Game(screen)
    game.run()

    pygame.quit()