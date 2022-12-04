# Advent of Code 2022
# https://adventofcode.com/2022
# Day 04

# Original solution --> see day04_muchBetter for a more elegant one

def load_txt(path):
    pairs_list = []
    with open(path, "r") as file:
        for line in file:
            pair_str = line.rstrip().split(",")   # Splits to e.g. ["2-4","6-8"]
            pair_split = [item.split("-") for item in pair_str]
            pair_tuple = [( int(interval[0]), int(interval[1]) ) for interval in pair_split]
            pairs_list.append(pair_tuple)
    return pairs_list

def isContained(ass_pair):
    ass_pair = sorted(ass_pair, key=lambda x: x[0])
    # For cases when the first section number is equal, 
    # e.g. [(44,63),(44,62)] is first sorted as [(44,62),(44,63)]
    # but to make it work, it needs to be reversed back to [(44,63),(44,62)]
    ass_pair = sorted(ass_pair, key=lambda x: x[1], reverse=True)
    elf1_sections = ass_pair[0]
    elf2_sections = ass_pair[1]
    return elf1_sections[0] <= elf2_sections[0] and elf1_sections[1] >= elf2_sections[1]

def isOverlapping(ass_pair):
    ass_pair = sorted(ass_pair)
    elf1_sections = ass_pair[0]
    elf2_sections = ass_pair[1]
    return elf1_sections[1] >= elf2_sections[0]


if __name__ == "__main__":
    input_path = "input.txt"
    ass_pairs = load_txt(input_path)

    # Part 1:
    fully_contained_pairs = [pair for pair in ass_pairs if isContained(pair)]
    print(f"Part 1: {len(fully_contained_pairs)}")

    # Part 2:
    overlapping_pairs = [pair for pair in ass_pairs if isOverlapping(pair)]
    print(f"Part 1: {len(overlapping_pairs)}")