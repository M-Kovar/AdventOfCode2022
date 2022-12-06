# Advent of Code 2022
# https://adventofcode.com/2022
# Day 06

def load_txt(path):
    with open(path, "r") as file:
        return file.read().rstrip()

def get_marker_index(signal, marker_len=4):
    for i in range(marker_len,len(signal)):
        # Unwrap string into a list of characters
        seq = [*signal[i-marker_len:i]]
        isMarker = len(set(seq)) == marker_len
        if isMarker:
            return i


if __name__ == "__main__":
    input_path = "input.txt"
    signal = load_txt(input_path)

    # Part 1:
    print(f"Part 1: {get_marker_index(signal)}")

    # Part 2:
    print(f"Part 2: {get_marker_index(signal, marker_len=14)}")