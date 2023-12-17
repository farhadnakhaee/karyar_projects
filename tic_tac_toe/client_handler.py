import json


class ClientHandler:
    def __init__(self, connections):
        self.connections = connections
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.send_board()

    def handel_client(self):
        client = self.connections[0]
        player = self.players[0]
        while True:
            data = client.recv(1024).decode("utf-8")
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
                    client = self.connections[1] if client == self.connections[0] else self.connections[0]
                    player = "O" if player == "X" else "X"
                     
    def check_win(self, board):
        # todo: check win
        pass

    def check_tie(self, board):
        # todo: check tie
        pass

    def send_board(self):
        print(self.connections)
        for connection in self.connections:
            data = json.dumps({'board': self.board})
            connection.send(data.encode("utf-8"))




