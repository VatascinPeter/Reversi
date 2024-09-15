
class MyPlayer:
    """Plays to get as much points every round. Hopefully."""
    def __init__(self, my_colour, opponent_colour):
        self.my_colour = my_colour
        self.opponent_colour = opponent_colour
        self.name = 'vataspet'
        self.directions = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 == j:
                    pass
                else:
                    self.directions.append((i, j))

    def move(self, board):
        legal_moves = {}
        play_move = ()
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == self.my_colour:
                    for q in range(len(self.directions)):
                        distance = 1
                        enemy_line = 0
                        while 1:
                            r = row + self.directions[q][0] * distance
                            c = column + self.directions[q][1] * distance
                            if r < 0 or c < 0 or r > 7 or c > 7 or board[r][c] == self.my_colour:
                                break
                            if board[r][c] == self.opponent_colour:
                                enemy_line += 1
                            if board[r][c] == -1:
                                if enemy_line > 0:
                                    if legal_moves.get((r, c)) is None:
                                        legal_moves[(r, c)] = enemy_line
                                    else:
                                        legal_moves[(r, c)] = legal_moves.get((r, c)) + enemy_line
                                break
                            distance += 1
        best_value = -999
        for coord, value in legal_moves.items():
            if value > best_value:
                best_value = value
                play_move = coord

        return None if len(legal_moves) == 0 else play_move


if __name__ == "__main__":
    player = MyPlayer(1, 0)
    pole = ((-1, -1, -1, -1, -1, -1, -1, -1),
             (-1, -1, -1, -1, -1, -1, -1, -1),
             (-1, -1, -1, 1, 0, -1, -1, -1),
             (-1, -1, -1, 1, 0, 0, -1, -1),
             (-1, -1, 1, 0, 1, 0, -1, -1),
             (-1, -1, 0, -1, -1, 0, -1, -1),
             (-1, 1, -1, -1, -1, 1, -1, -1),
             (-1, -1, -1, -1, -1, -1, -1, -1))
    print(player.move(pole))
