# Advent of Code 2022
# https://adventofcode.com/2022
# Day 04

# Much better solution, based on an advice to use ranges and sets

def load_txt(path):
    pairs_list = []
    with open(path, "r") as file:
        for line in file:
            pair_str = line.rstrip().split(",")   # Splits to e.g. ["2-4","6-8"]
            pair_split = [item.split("-") for item in pair_str]
            pair_range = [range(int(interval[0]), int(interval[1])+1) for interval in pair_split]
            pairs_list.append(pair_range)
    return pairs_list

def isContained(ass_pair):
    elf1_set = set(ass_pair[0])
    elf2_set = set(ass_pair[1])
    return elf1_set.issubset(elf2_set) or elf2_set.issubset(elf1_set)
    
def isOverlapping(ass_pair):
    return set(ass_pair[0]) & set(ass_pair[1])


if __name__ == "__main__":
    input_path = "input.txt"
    ass_pairs = load_txt(input_path)
    print(ass_pairs)
    # Part 1:
    fully_contained_pairs = [pair for pair in ass_pairs if isContained(pair)]
    print(f"Part 1: {len(fully_contained_pairs)}")

    # Part 2:
    overlapping_pairs = [pair for pair in ass_pairs if isOverlapping(pair)]
    print(f"Part 1: {len(overlapping_pairs)}")