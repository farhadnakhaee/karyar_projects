import socket
import threading
from client_handler import ClientHandler


class Server:
    def __init__(self, server_address):
        self.connections = []
        self.client_handler = ClientHandler()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(server_address)
        self.server_socket.listen(5)
        self.players = ["X", "O"]

    def start_server(self):
        for i in range(2):
            client, addr = self.server_socket.accept()
            self.connections.append(client)
            print(f"connected {addr}")
            thread = threading.Thread(target=self.client_handler.handel_client, args=(client, self.players[i]))
            thread.start()


