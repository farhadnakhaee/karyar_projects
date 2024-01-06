import sys
import pygame
from setting import Setting


class GameRenderer:
    def __init__(self):
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_height, self.setting.screen_width))
        pygame.display.set_caption("Tic Tac Toe")

    def draw_grid(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.setting.line_color,
                             (i * self.setting.screen_width // 3, 0),
                             (i * self.setting.screen_width // 3, self.setting.screen_height), 3)
            pygame.draw.line(self.screen, self.setting.line_color,
                             (0, i * self.setting.screen_height // 3),
                             (self.setting.screen_width, i * self.setting.screen_height // 3), 3)

    def draw_shapes(self, board):
        for row in range(3):
            for col in range(3):
                if board[row][col] == "X":
                    self._draw_cross(row, col)
                elif board[row][col] == "O":
                    self._draw_circle(row, col)

    def _draw_circle(self, row, col):
        center = (self.setting.cell_width * (row + 1 / 2), self.setting.cell_height * (col + 1 / 2))
        radius = self.setting.radius_of_circle
        pygame.draw.circle(self.screen, self.setting.circle_color, center, radius, 10)

    def _draw_cross(self, row, col):
        x1 = self.setting.cell_width / 4
        y1 = self.setting.cell_height / 4
        x2 = 3 * x1
        y2 = 3 * y1
        pygame.draw.line(self.screen, self.setting.cross_color,
                         (self.setting.cell_width * row + x1, self.setting.cell_height * col + y1),
                         (self.setting.cell_width * row + x2, self.setting.cell_height * col + y2),
                         10)
        pygame.draw.line(self.screen, self.setting.cross_color,
                         (self.setting.cell_width * row + x2, self.setting.cell_height * col + y1),
                         (self.setting.cell_width * row + x1, self.setting.cell_height * col + y2),
                         10)

    def draw_turn_light(self, color):
        pygame.draw.circle(self.screen, color, (30, 30), 15)

    def render_board(self, board, turn, player):
        self.screen.fill(self.setting.bg_color)
        self.draw_grid()
        self.draw_shapes(board)
        if turn == player:
            self.draw_turn_light(self.setting.green)
        else:
            self.draw_turn_light(self.setting.red)
        pygame.display.flip()

    def get_action(self):
        """I know this method should not be here but the actions of game is small."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_y // self.setting.cell_height
                row = mouse_x // self.setting.cell_width
                return row, col

