# Advent of Code 2022
# https://adventofcode.com/2022
# Day 05

import re
import copy

def load_crates_moves(path):
    with open(path, "r") as file:
        lines = file.readlines()
        idx_separator = lines.index("\n")
        crates, moves = lines[:idx_separator], lines[idx_separator+1:]
        return (crates, moves)

def get_crates_scheme(lines_crates):
    # How: find positions of stack numbers, then just find in each row the same indices
    scheme = dict()
    # Get the line with stack numbers
    line_stack_nums = lines_crates.pop()
    # Find stack numbers and indexes in string
    stack_nums = [int(res) for res in re.findall(r"\d", line_stack_nums)]
    stack_inline_idx = [res.span()[0] for res in re.finditer(r"\d", line_stack_nums)]
    # Initialize dict for the scheme
    scheme = {stack_num: [] for stack_num in stack_nums}
    # Fill the scheme with crates
    for line in reversed(lines_crates):
        crates = [line[i] for i in stack_inline_idx]
        for stack_num, crate in zip(stack_nums, crates):
            if crate != " ":
                scheme[stack_num].append(crate)
    return scheme

def get_moves_scheme(lines_crates):
    scheme = []
    for line in lines_crates:
        numbers = re.findall(r"\d+", line)
        scheme.append(tuple([int(num) for num in numbers]))
    return scheme

def move_crates(crates_scheme, moves_scheme, method=""):
    crates_scheme_moved = copy.deepcopy(crates_scheme)
    for move in moves_scheme:
        num, frm, to = move
        moved_crates = crates_scheme_moved[frm][-num:]
        if method != "CrateMover 9001":
            moved_crates = reversed(moved_crates)
        del crates_scheme_moved[frm][-num:]
        crates_scheme_moved[to].extend(list(moved_crates))
    return crates_scheme_moved

def get_top_crates(crates_scheme, string_output=False):
    top_crates = [val[-1] for val in crates_scheme.values() if val]
    # If requested, return as a string:
    if string_output:
        return ''.join(top_crates)
    return top_crates

if __name__ == "__main__":
    input_path = "input.txt"
    lines_crates, lines_moves = load_crates_moves(input_path)

    crates_scheme = get_crates_scheme(lines_crates)
    moves_scheme = get_moves_scheme(lines_moves)

    # Part 1:
    moved_crates1 = move_crates(crates_scheme, moves_scheme)
    print(f"Part 1: {get_top_crates(moved_crates1, string_output=True)}")

    # Part 2:
    moved_crates2 = move_crates(crates_scheme, moves_scheme, method="CrateMover 9001")
    print(f"Part 2: {get_top_crates(moved_crates2, string_output=True)}")