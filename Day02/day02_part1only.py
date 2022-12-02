# Advent of Code 2022
# https://adventofcode.com/2022
# Day 02

def load_txt(path):
    with open(path, "r") as file:
        input_list = [tuple(line.rstrip().split(" ")) for line in file]
    return input_list

class RPS_game:
    
    def __init__(self, moves_list):
        self.moves_list = moves_list

        self.scoring_symbols = {
            "X": 1,
            "Y": 2,
            "Z": 3
        }

        self.scoring_matches = {
            "win": 6,
            "draw": 3,
            "lose": 0
        }

        self.wins = [
            ("C", "X"),
            ("A", "Y"),
            ("B", "Z")
        ]

        self.draws = [
            ("A", "X"),
            ("B", "Y"),
            ("C", "Z")
        ]

    def score_pair(self, pair):
        score = self.scoring_symbols[pair[1]]
        if pair in self.wins:
            score += self.scoring_matches["win"]
        elif pair in self.draws:
            score += self.scoring_matches["draw"]
        else:
            score += self.scoring_matches["lose"]
        return score

    def get_scores(self):
        return [self.score_pair(pair) for pair in self.moves_list]

    def get_total_score(self):
        return sum(self.get_scores())


if __name__ == "__main__":
    input_path = "input.txt"
    moves_list = load_txt(input_path)

    game = RPS_game(moves_list)
    total_score = game.get_total_score()
    print(total_score)