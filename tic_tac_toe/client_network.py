import json
import socket
import pickle
import pygame.event
from setting import Setting
import game_renderer
import sys


class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.renderer = game_renderer.GameRenderer()
        # self.setting = Setting()
        # self.event_processed = False

    def connect_to_server(self, server_address):
        self.client_socket.connect(server_address)

    # def start_client(self):
    #     while True:
    #         self.event_processed = False
    #         data = self.client_socket.recv(1024).decode("utf-8")
    #         if not data:
    #             break
    #
    #         game_state = json.loads(data)
    #         board = game_state["board"]
    #         self.renderer.render(board)
    #
    #         row, col = self.get_move()
    #         self.send_move(row, col)

    def receive_game_state(self):
        data = self.client_socket.recv(1024).decode("utf-8")
        game_state = json.loads(data)
        board = game_state["board"]
        turn = game_state["turn"]
        return board, turn

    def receive_player_symbol(self):
        symbol = self.client_socket.recv(1024).decode("utf-8")
        return symbol

    def send_move(self, row, col):
        move = {'row': row, 'col': col}
        self.client_socket.send(json.dumps(move).encode('utf-8'))



