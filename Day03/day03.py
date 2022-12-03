# Advent of Code 2022
# https://adventofcode.com/2022
# Day 03

def load_txt(path):
    with open(path, "r") as file:
        input_list = [line.rstrip() for line in file]
    return input_list

def split_into_compartments(items_in_rucksacks):
    items_split = []
    for items in items_in_rucksacks:
        half = int(len(items)/2)
        items_split.append((items[:half], items[half:]))
    return items_split

def get_common_item(rucksack):
    # Common element found using sets, then extracted from the created single-item set
    return list( set(rucksack[0]) & set(rucksack[1]) )[0]

def get_priority(item):
    # For conversion from ASCII index to elf priority
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    upper_idx_first = 65
    lower_idx_first = 97
    upper_score_shift = 26
    isUpper = item == item.upper()
    # Calculate based on ASCII index
    if isUpper:
        priority = ord(item) - (upper_idx_first-1) + upper_score_shift
    else:
        priority = ord(item) - (lower_idx_first-1)
    return priority

def find_badges(items_list):
    badges = []
    for i in range(0,len(items_list),3):
        group = items_list[i:i+3]
        # Common element found using sets, then extracted from the created single-item set
        badges.append( list( set(group[0]) & set(group[1]) & set(group[2]) )[0] )
    return badges
        

if __name__ == "__main__":
    input_path = "input.txt"
    items_list = load_txt(input_path)
    items_split = split_into_compartments(items_list)

    common_items = [get_common_item(rucksack) for rucksack in items_split]

    # Part 1:
    priorities = [get_priority(item) for item in common_items]
    print(f"Part 1: {sum(priorities)}")

    # Part 2:
    badges = find_badges(items_list)
    priorities_badge = [get_priority(badge) for badge in badges]
    print(f"Part 2: {sum(priorities_badge)}")