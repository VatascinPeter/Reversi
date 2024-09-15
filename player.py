import copy


class MyPlayer:
    """This player seems really greedy, but uses brain to foresee future as well"""
    def __init__(self, my_colour, opponent_colour):
        self.my_colour = my_colour
        self.opponent_colour = opponent_colour
        self.name = 'vataspet'
        self.directions = []
        self.round = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 == j:
                    pass
                else:
                    self.directions.append((i, j))

    def pick_move(self, available_moves):
        """From dictionary of possible moves and their value picks the most valuable"""
        best_move = None
        best_value = None
        if available_moves:
            counter = 0
            for coord, value in available_moves.items():
                if not counter:
                    best_move = coord
                    best_value = value
                elif value > best_value:
                    best_move = coord
                    best_value = value
                counter += 1
        best_tuple = (best_move, best_value)
        return best_tuple

    def find_best_move(self, board, colour, iterations):
        """Searches for possible moves and gives them value based on
         their position, possible opponents moves and pieces converted"""
        legal_moves = {}
        other_colour = 0 if colour else 1
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == colour:
                    for direction_number in range(len(self.directions)):
                        distance = 1
                        enemy_line = 0
                        while 1:
                            r = row + self.directions[direction_number][0] * distance
                            c = column + self.directions[direction_number][1] * distance
                            if r < 0 or c < 0 or r > 7 or c > 7 or board[r][c] == colour:
                                break
                            if board[r][c] == other_colour:
                                enemy_line += 1
                            if board[r][c] == -1:
                                if enemy_line > 0:
                                    if not legal_moves.get((r, c)):
                                        legal_moves[(r, c)] = enemy_line
                                        if (r == 0 or r == 7) and (c == 0 or c == 7):
                                            legal_moves[(r, c)] = legal_moves.get((r, c)) + 100
                                        elif r == 0 or r == 7 or c == 0 or c == 7:
                                            legal_moves[(r, c)] = legal_moves.get((r, c)) + 20

                                        if iterations > 0:
                                            next_board = copy.deepcopy(board)
                                            next_board[r][c] = colour
                                            next_value = self.find_best_move(next_board, 0 if colour else 1, iterations - 1)[1]
                                            if next_value:
                                                legal_moves[(r, c)] = legal_moves.get((r, c)) - next_value / 2
                                            else:
                                                legal_moves[(r, c)] = legal_moves.get((r, c)) + 1023
                                    else:
                                        legal_moves[(r, c)] = legal_moves.get((r, c)) + enemy_line
                                break
                            distance += 1

        return self.pick_move(legal_moves)

    def move(self, board):
        self.round += 1
        if 2 < self.round < 25:
            iterations = 3
        else:
            iterations = 4
        return self.find_best_move(board, self.my_colour, iterations)[0]
