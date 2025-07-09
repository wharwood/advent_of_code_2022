from enum import Enum

class rps_move:
    def __init__(self, move: str, result: str):
        self.move = opponent_move(move)
        self.outcome = outcome(result)
        self.response = self.get_response()
        self.score = self.get_score()

    def get_response(self):
        if self.move == opponent_move.rock and self.outcome == outcome.win:
            return response_move.paper
        elif self.move == opponent_move.rock and self.outcome == outcome.draw:
            return response_move.rock
        elif self.move == opponent_move.rock and self.outcome == outcome.lose:
            return response_move.scissors
        elif self.move == opponent_move.paper and self.outcome == outcome.win:
            return response_move.scissors
        elif self.move == opponent_move.paper and self.outcome == outcome.draw:
            return response_move.paper
        elif self.move == opponent_move.paper and self.outcome == outcome.lose:
            return response_move.rock
        elif self.move == opponent_move.scissors and self.outcome == outcome.win:
            return response_move.rock
        elif self.move == opponent_move.scissors and self.outcome == outcome.draw:
            return response_move.scissors
        elif self.move == opponent_move.scissors and self.outcome == outcome.lose:
            return response_move.paper

    def get_score(self) -> int:
        if self.move == opponent_move.rock and self.response == response_move.rock:
            return 1 + 3
        elif self.move == opponent_move.rock and self.response == response_move.paper:
            return 2 + 6
        elif self.move == opponent_move.rock and self.response == response_move.scissors:
            return 3 + 0
        elif self.move == opponent_move.paper and self.response == response_move.rock:
            return 1 + 0
        elif self.move == opponent_move.paper and self.response == response_move.paper:
            return 2 + 3
        elif self.move == opponent_move.paper and self.response == response_move.scissors:
            return 3 + 6
        elif self.move == opponent_move.scissors and self.response == response_move.rock:
            return 1 + 6
        elif self.move == opponent_move.scissors and self.response == response_move.paper:
            return 2 + 0
        elif self.move == opponent_move.scissors and self.response == response_move.scissors:
            return 3 + 3

class rps_game:
    def __init__(self, moves: list[rps_move]):
        self.moves = moves
        self.total_score = sum([move.score for move in moves])

class opponent_move(Enum):
    rock = 'A'
    paper = 'B'
    scissors = 'C'

class response_move(Enum):
    rock = 'X'
    paper = 'Y'
    scissors = 'Z'

class outcome(Enum):
    lose = 'X'
    draw = 'Y'
    win = 'Z'

def do_part_1(input: list[str]):
    game = get_game(input)
    print(game.total_score)

def do_part_2(input: list[str]):
    game = get_game(input)
    print(game.total_score)

def get_game(raw_moves: list[str]):
    moves = []
    for line in raw_moves:
        moves.append(rps_move(line[0],line[2]))
    return rps_game(moves)