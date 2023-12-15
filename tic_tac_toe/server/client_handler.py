import json


class ClientHandler:
    def __init__(self):
        self.connections = []
        self.board = [["" for _ in range(3)] for _ in range(3)]

    def handel_client(self, client_socket, player):
        while True:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break

            move = json.loads(data)
            row, col = move["row"], move["col"]

            if self.board[row][col] == "":
                self.board[row][col] = player
                self.send_board()
                if self.check_win(self.board):
                    print(f"Player {player} wins!")
                    break
                elif self.check_tie(self.board):
                    print("It's tie!")
                    break
                else:
                    player = "O" if player == "X" else "X"

    def check_win(self, board):
        # todo: check win
        pass

    def check_tie(self, board):
        # todo: check tie
        pass

    def send_board(self):
        data = json.dumps({'board': self.board})
        for connection in self.connections:
            connection.send(data.encode("utf-8"))




