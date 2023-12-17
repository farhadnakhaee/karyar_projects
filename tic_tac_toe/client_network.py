import json
import socket
import pygame.event
from setting import Setting
import game_renderer
import sys


class Client:
    def __init__(self, server_address):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(server_address)
        self.renderer = game_renderer.GameRenderer()
        self.setting = Setting()
        self.event_processed = False

    def start_client(self):
        while True:
            self.event_processed = False
            data = self.client_socket.recv(1024).decode("utf-8")
            if not data:
                break
            
            game_state = json.loads(data)
            board = game_state["board"]
            self.renderer.render(board)

            row, col = self.get_move()
            self.send_move(row, col)

    def get_move(self):
        while not self.event_processed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    col = mouse_y // self.setting.cell_height
                    row = mouse_x // self.setting.cell_width
                    self.event_processed = True
                    return row, col

    def send_move(self, row, col):
        move = {'row': row, 'col': col}
        self.client_socket.send(json.dumps(move).encode('utf-8'))


