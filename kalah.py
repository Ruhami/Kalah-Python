class Kalah(object):
    def __init__(self, holes, seeds):
        self.player = 0
        self.holes = holes
        self.len_board = holes * 2 + 2
        self.places = [range(holes), range(holes + 1, holes * 2 + 1)]
        self.seeds = seeds
        self.kal = [holes, self.len_board - 1]
        self.board = [0 if i in self.kal else self.seeds for i in range(self.len_board)]

    def __repr__(self):
        return f"Kalah({self.seeds}, {self.holes}, status={self.status()}, player={self.player})"

    def play(self, hole):
        if self.done():
            return self.win()

        if self.kal[1] < hole or hole < 0:
            raise IndexError("This hole number not exist in this Kalah board!")

        if hole not in self.places[self.player]:
            raise IndexError("You are not allowed to play in this hole!")

        if self.board[hole] == 0:
            raise ValueError("You are trying to play empty hole")

        competitor_kal = self.kal[-1 * self.player + 1]
        seeds = self.board[hole]
        self.board[hole] = 0
        for i in range(1, seeds + 1):
            last_hole = (hole + i) % self.len_board
            if last_hole == competitor_kal:
                hole += 1
                last_hole = (hole + i) % (self.len_board)
            self.board[last_hole] += 1


        ops = (self.len_board - 2) - last_hole
        if self.board[last_hole] == 1 and last_hole in self.places[self.player] and self.board[ops] != 0:
            self.board[self.kal[self.player]] += 1 + self.board[ops]
            self.board[ops] = 0
            self.board[last_hole] = 0

        if last_hole not in self.kal:
            self.player = -1 * self.player + 1

        return f"Player {self.player + 1} plays next"

    def status(self):
        return tuple(self.board)

    def done(self):
        empty_holes = [0] * self.holes
        player_holes = self.places[self.player]
        if self.board[player_holes[0]:player_holes[-1] + 1] == empty_holes:
            self.player = -1 * self.player + 1
            c_holes = self.places[self.player]
            for i in c_holes:
                self.board[self.kal[self.player]] += self.board[i]
                self.board[i] = 0
            return True
        return False

    def score(self):
        return [self.board[self.kal[0]], self.board[self.kal[1]]]

    def win(self):
        scores = self.score()
        if scores[0] == scores[1]:
            return "Tie"
        win_player = scores.index(max(scores))
        return f"Player {win_player + 1} wins."

    def set_player(self, p):
        self.player = p

    def set_status(self, new_board):
        self.board = new_board

    def __str__(self):
        return self.render()

    def render(self):
        result = "\tP L A Y E R  2\n"
        result += f" {'______' * (self.holes+4)}\n"
        result += f"|★★★★{'  ____  '*self.holes}  ★★★★|\n"
        result += "|★   ★ "
        for elem in range(self.holes -1, -1, -1):
            result += f"[_{str(self.board[self.holes+1+elem])}__] \t"
        result += "★   ★|\n"
        result += "|★ " + str(self.board[self.kal[1]]) + " ★" + "  ____  "*self.holes + f""" ★ {str(self.board[self.kal[0]])} ★| \n"""
        result += f"""|★★★★\t"""
        for elem in self.board[0:self.holes]:
            result += "[" + f"_{str(elem)}__" + "]\t"
        result += "★★★★|\n"
        result += f" { '______' * (self.holes+4)}\n"
        result += "\tP L A Y E R  1"
        return result