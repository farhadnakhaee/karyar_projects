import json
import socket
import pygame.event
from karyar_projects.tic_tac_toe.server import setting
import game_renderer


class Client:
    def __init__(self, server_address):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(server_address)
        self.renderer = game_renderer.GameRenderer()
        self.setting = setting.Setting()

    def start_client(self):
        while True:
            data = self.client_socket.recv(1024).decode("utf-8")
            if not data:
                break

            game_state = json.loads(data)
            board = game_state["board"]
            self.renderer.render(board)
            row, col = self.get_move()
            self.send_move(row, col)

    def get_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // self.setting.cell_height
                col = mouse_x // self.setting.cell_width
                return row, col

    def send_move(self, row, col):
        move = {'row': row, 'col': col}
        self.client_socket.send(json.dumps(move).encode('utf-8'))


