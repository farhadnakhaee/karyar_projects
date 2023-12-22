import json
import socket
import threading

from server_network import Server
from game_logic import GameLogic


class Main:
    def __init__(self, server_address):
        self.server_address = server_address
        self.server = Server(server_address)
        self.connections = self.server.connections
        self.server.wait_for_clients()
        self.server.send_player_symbol()
        self.game_logic = GameLogic(self.connections)
        self.game_ended = False

    def run(self):
        while not self.game_ended:
            data_x = self.receive_from_x()
            data_o = self.receive_from_o()
            if data_x:
                self.protocol(action=data_x["action"], data=data_x["data"], player=data_x["player"])
            if data_o:
                self.protocol(action=data_o["action"], data=data_o["data"], player=data_o["player"])
        self.server.server_socket.close()

    def receive_from_x(self):
        data = self.connections["X"].recv(1024).decode("utf-8")
        if data:
            data = json.loads(data)
            return data

    def receive_from_o(self):
        data = self.connections["O"].recv(1024).decode("utf-8")
        if data:
            data = json.loads(data)
            return data

    def protocol(self, action, data, player):
        client = self.connections[player]
        turn = self.game_logic.get_turn()

        if action == "game_state":
            self.server.send_game_state(client, self.game_logic.board, turn)

        elif action == "move":
            move = data
            self.game_logic.update_board(move[0], move[1], player)

            if self.game_logic.check_win(player):
                self.server.send_massage(client, "YOU WIN!")
                self.game_ended = True

            if self.game_logic.check_tie():
                self.server.send_massage(client, "TIE!")
                self.game_ended = True

            self.game_logic.change_turn()
            self.server.send_massage(client, "move in server completed", move)


if __name__ == "__main__":
    server_addr = ('localhost', 8888)
    main = Main(server_addr)
    main.run()
