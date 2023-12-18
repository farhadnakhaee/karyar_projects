import json
import socket
import pickle
import threading
from client_handler import ClientHandler


class Server:
    def __init__(self, server_address):
        self.connections = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(server_address)
        self.server_socket.listen()
        self.players = ["X", "O"]

    def wait_for_clients(self):
        i = -1
        while len(self.connections) < 2:
            client, addr = self.server_socket.accept()
            i += 1
            self.connections[self.players[i]] = client
            print(f"connected {addr}")

    def send_game_state(self, board, player):
        for connection in self.connections.values():
            data = json.dumps({'board': board, 'turn': player})
            connection.send(data.encode("utf-8"))

    def send_player_symbol(self):
        for symbol, connection in self.connections.items():
            connection.send(symbol.encode("utf-8"))

    def receive_move(self, client):
        data = client.recv(1024).decode("utf-8")
        move = json.loads(data)
        row, col = move["row"], move["col"]
        return row, col




