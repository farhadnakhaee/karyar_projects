import json
import socket


class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self, server_address):
        self.client_socket.connect(server_address)

    def get(self, action, data, player):
        request = json.dumps({'action': action, "data": data, "player": player})
        self.client_socket.send(request.encode())
        response = self.client_socket.recv(1024).decode("utf-8")
        response = json.loads(response)
        return response

    def receive_player_symbol(self):
        symbol = self.client_socket.recv(1024).decode("utf-8")
        return symbol
