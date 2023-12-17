import socket
import threading
from client_handler import ClientHandler


class Server:
    def __init__(self, server_address):
        self.connections = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(server_address)
        self.server_socket.listen()

    def connect_to_server(self):
        while len(self.connections) < 2:
            client, addr = self.server_socket.accept()
            self.connections.append(client)
            print(f"connected {addr}")
    
    def start_game(self):
        client_handler = ClientHandler(self.connections)
        client_handler.handel_client()


