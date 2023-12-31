import json
import socket


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

    def send_game_state(self, client, board, player):
        data = json.dumps({'board': board, 'turn': player})
        client.send(data.encode("utf-8"))

    def send_massage(self, client, massage, data=None):
        report = json.dumps({'massage': massage, "data": data})
        client.send(report.encode("utf-8"))

    def send_player_symbol(self):
        for symbol, connection in self.connections.items():
            connection.send(symbol.encode("utf-8"))

    def receive_move(self, client):
        data = client.recv(1024).decode("utf-8")
        move = json.loads(data)
        row, col = move["row"], move["col"]
        return row, col




