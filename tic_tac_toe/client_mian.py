from client_network import Client
from game_renderer import GameRenderer

server_address = ('localhost', 8888)
client = Client()

# connect to server
client.connect_to_server(server_address)

# receive client's symbol
player_symbol = client.receive_player_symbol()

# initialize GameRender
game_render = GameRenderer()

connected = True

while connected:
    # receive board / wait to receive
    board, turn = client.receive_game_state()

    # render board
    game_render.render(board)

    if player_symbol == turn:
        # get action (mouse button position or exit)
        row, col = game_render.get_action()

        # send move
        client.send_move(row, col)

# receive results.
# print it.
