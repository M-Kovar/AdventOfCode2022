# Advent of Code 2022
# https://adventofcode.com/2022
# Day 01

def load_txt(path):
    with open(path, "r") as file:
        input_list = [line.rstrip() for line in file]
    return input_list

def get_calories_per_elf(calories_list):
    calories_per_elf = []
    cal_sum = 0
    for row in calories_list:
        if row:
            cal_sum += int(row)
        else:
            calories_per_elf.append(cal_sum)
            cal_sum = 0
    return calories_per_elf

def get_top_calories(calories_list, num_top):
    return sorted(calories_list, reverse=True)[:num_top]


if __name__ == "__main__":
    input_path = "input.txt"
    input_raw = load_txt(input_path)
    cal_per_elf = get_calories_per_elf(input_raw)

    # Part 1:
    print(f"Top Elf: {max(cal_per_elf)}")

    # Part 2:
    print(f"Top 3 Elfs: {sum(get_top_calories(cal_per_elf, num_top=3))}")