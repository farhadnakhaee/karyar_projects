from client_network import Client
from game_renderer import GameRenderer


class Main:
    def __init__(self, server_address):
        self.server_address = server_address
        self.client = Client()
        self.client.connect_to_server(server_address)
        self.player_symbol = self.client.receive_player_symbol()
        self.game_render = GameRenderer()
        self.connected = True

    def run(self):
        while self.connected:
            response = self.client.get("game_state", "None", self.player_symbol)
            board = response["board"]
            turn = response["turn"]
            self.game_render.render_board(board, turn, self.player_symbol)

            move = self.game_render.get_action()
            if move and self.player_symbol == turn:
                response = self.client.get("move", move, self.player_symbol)
                massage = response["massage"]

                if massage == "YOU WIN!" or massage == "TIE!":
                    print(massage)
                    self.connected = False


if __name__ == "__main__":
    server_addr = ('localhost', 8888)
    main = Main(server_addr)
    main.run()
