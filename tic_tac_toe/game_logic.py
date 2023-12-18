
class GameLogic:
    def __init__(self, board, connections):
        self.board = board
        self.connections = connections
        self.client = None

    def check_win(self):
        pass

    def check_tie(self):
        pass

    def check_game_ended(self):
        return False

    def get_turn(self):
        if self.client == self.connections["X"]:
            self.client = self.connections["O"]
            return self.client, "O"
        else:
            self.client = self.connections["X"]
            return self.client, "X"

    def update_board(self, row, col, player):
        if self.board[row][col] == "":
            self.board[row][col] = player
            return self.board
