from kalah import Kalah


def parse_game(lines):
    steps = []
    banks = []
    num_board = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "bank1": 6, "A": 7, "B": 8, "C": 9, "D": 10, "E": 11,
                 "F": 12, "bank2": 13}
    for line in lines:
        for s in line[3:].split():
            x = s.split("-")
            for step in x:
                steps.append(num_board[step[0]])
            if len(x[-1]) > 2:
                banks.append(x[-1][3])
            else:
                banks.append("0")
    return [steps, banks]


def simulate_game(holes, seeds, steps):
    result = []
    game = Kalah(holes, seeds)

    for step in steps:
        result.append((game.play(step), game.status()))
    return result


def render_game(holes, seeds, steps):
    pass


if __name__ == "__main__":
    pass
    # with open(f"data/game_2.txt") as f:
    #     lines = f.read().splitlines()
    # steps = parse_game(lines)
    # print(render_game(6, 6, steps))
