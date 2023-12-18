from server_network import Server
from game_logic import GameLogic

# initialize server
server_address = ('localhost', 8888)
server = Server(server_address)
connections = server.connections

# two player must be connected to server.
server.wait_for_clients()
print("two player connected.")

# It sends symbols to the players so that they know whose turn it is
server.send_player_symbol()

# initialize board
board = [["" for _ in range(3)] for _ in range(3)]

# initialize GameLogic
game_logic = GameLogic(board, connections)

game_ended = False

while not game_ended:
    # check game_ended (win or tie or exit)
    # if win or tie or exit write data to a file.
    game_ended = game_logic.check_game_ended()
    if game_ended:
        pass

    # get turns to player
    client, player = game_logic.get_turn()

    # send board for players.
    server.send_game_state(board, player)

    # receive move from client whose turn it is. / wait to receive
    row, col = server.receive_move(client)

    # update board
    board = game_logic.update_board(row, col, player)

# read file.
# send results to clients.
