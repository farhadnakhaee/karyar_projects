
class GameLogic:
    def __init__(self, connections):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.connections = connections
        self.turn = "X"

    def check_win(self, player):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True

    def check_game_ended(self):
        return False

    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def get_turn(self):
        return self.turn

    def update_board(self, row, col, player):
        if self.board[row][col] == "":
            self.board[row][col] = player
            return self.board
