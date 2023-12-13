import pygame
from setting import Setting


class TicTacToe:
    def __init__(self):
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_height, self.setting.screen_width))
        pygame.display.set_caption("Tic Tac Toe")
        self.board = [["X" for _ in range(3)] for _ in range(3)]

    def draw_grid(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.setting.line_color,
                             (i * self.setting.screen_width // 3, 0),
                             (i * self.setting.screen_width // 3, self.setting.screen_height), 3)
            pygame.draw.line(self.screen, self.setting.line_color,
                             (0, i * self.setting.screen_height // 3),
                             (self.setting.screen_width, i * self.setting.screen_height // 3), 3)

    def draw_shapes(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "X":
                    self._draw_cross(row, col)
                elif self.board[row][col] == "O":
                    self._draw_circle(row, col)

    def _draw_circle(self, row, col):
        center = (self.setting.cell_width * (row + 1 / 2), self.setting.cell_height * (col + 1 / 2))
        radius = self.setting.radius_of_circle
        pygame.draw.circle(self.screen, self.setting.circle_color, center, radius, 6)

    def _draw_cross(self, row, col):
        x1 = self.setting.cell_width / 4
        y1 = self.setting.cell_height / 4
        x2 = 3 * x1
        y2 = 3 * y1
        pygame.draw.line(self.screen, self.setting.cross_color,
                         (self.setting.cell_width * row + x1, self.setting.cell_height * col + y1),
                         (self.setting.cell_width * row + x2, self.setting.cell_height * col + y2),
                         6)
        pygame.draw.line(self.screen, self.setting.cross_color,
                         (self.setting.cell_width * row + x2, self.setting.cell_height * col + y1),
                         (self.setting.cell_width * row + x1, self.setting.cell_height * col + y2),
                         6)


# tic_tac = TicTacToe()
# tic_tac.screen.fill(tic_tac.setting.bg_color)
# tic_tac.draw_grid()
# tic_tac.draw_shapes()
# pygame.display.update()
# while True:
#     pygame.event.pump()

