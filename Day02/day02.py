# Advent of Code 2022
# https://adventofcode.com/2022
# Day 02

def load_txt(path):
    with open(path, "r") as file:
        input_list = [tuple(line.rstrip().split(" ")) for line in file]
    return input_list

class RPS_game:
    
    def __init__(self, moves_list, method):
        self.moves_list = moves_list
        self.method = method

        self.scores_symbol = {
            "X": 1,
            "Y": 2,
            "Z": 3
        }

        self.scores_result = {
            "win": 6,
            "draw": 3,
            "lose": 0
        }

        self.win_pairs = {
            "A": "Y",
            "B": "Z",
            "C": "X"
        }

        self.draw_pairs = {
            "A": "X",
            "B": "Y",
            "C": "Z"
        }

        self.lose_pairs = {
            "A": "Z",
            "B": "X",
            "C": "Y"
        }

        self.result_to_pair = {
            "X": self.lose_pairs,
            "Y": self.draw_pairs,
            "Z": self.win_pairs
        }

    def get_pair_by_result(self, pair_with_result):
        their_symbol = pair_with_result[0]
        match_result = pair_with_result[1]
        pairs_dict = self.result_to_pair[match_result]
        our_symbol = pairs_dict[their_symbol]
        return (their_symbol, our_symbol)

    def score_pair(self, pair):
        # Adjust pair for part2:
        if self.method == "part2":
            pair = self.get_pair_by_result(pair)

        # Get score for our symbol:
        score = self.scores_symbol[pair[1]]

        # Increase score by match result:
        if pair in self.win_pairs.items():
            score += self.scores_result["win"]
        elif pair in self.draw_pairs.items():
            score += self.scores_result["draw"]
        else:
            score += self.scores_result["lose"]
        return score

    def get_scores(self):
        return [self.score_pair(pair) for pair in self.moves_list]

    def get_total_score(self):
        return sum(self.get_scores())


if __name__ == "__main__":
    input_path = "input.txt"
    moves_list = load_txt(input_path)

    # Part 1:
    game_part1 = RPS_game(moves_list, method="part1")
    total_score = game_part1.get_total_score()
    print(f"Part1 score: {total_score}")

    # Part 2:
    game_part2 = RPS_game(moves_list, method="part2")
    total_score2 = game_part2.get_total_score()
    print(f"Part2 score: {total_score2}")