# Advent of Code 2022
# https://adventofcode.com/2022
# Day 11
# Part 2 solved with a hint from Reddit after a long period of trials and desperation

import re
import math

def load_txt(path):
    notes = []
    notes_monkey = []
    with open(path, "r") as file:
        for line in file:
            if line == "\n":
                notes.append(notes_monkey)
                notes_monkey = []
                continue
            notes_monkey.append(line.rstrip())
        notes.append(notes_monkey)
    return notes

class Monkey():
    def __init__(self, instructions, relief_method="none"):
        self.num_inspections = 0
        self.relief_factor = 3 if relief_method=="part1" else 1
        self.relief_method = relief_method
        self.parse_instructions(instructions)

    def parse_instructions(self, instructions):
        self.id = int(re.findall(r"\d+", instructions[0])[0])
        self.items = [int(item) for item in re.findall(r"\d+", instructions[1])]
        self.operation = instructions[2].split("new = ")[1].replace("old", "item")
        self.test_divisible = int(re.findall(r"\d+", instructions[3])[0])
        self.if_true_throw  = int(re.findall(r"\d+", instructions[4])[0])
        self.if_false_throw = int(re.findall(r"\d+", instructions[5])[0])

    def execute_turn(self):
        to_throw = []
        for _ in range(len(self.items)):
            item = self.items.pop(0)
            item = self.inspect(item)
            throw_to_id = self.test(item)
            to_throw.append((throw_to_id, item))
        return to_throw

    def inspect(self, item):
        item = eval(self.operation)
        # Apply relief
        if self.relief_method in ["part1", "none"]:
            item //= self.relief_factor
        elif self.relief_method == "part2":
            item %= self.relief_factor
        self.num_inspections += 1
        return item

    def test(self, item):
        if item % self.test_divisible == 0:
            return self.if_true_throw
        else:
            return self.if_false_throw

class Monkey_simulator():
    def __init__(self, instructions_all, relief_method="none"):
        self.monkeys = [Monkey(instr, relief_method) for instr in instructions_all]
        if relief_method == "part2":
            relief_factor = self.get_common_relief_factor()
            for monkey in self.monkeys:
                monkey.relief_factor = relief_factor

    def run_rounds(self, count, print_progress=False):
        for i in range(count):
            for monkey in self.monkeys:
                to_throw = monkey.execute_turn()
                self.throw_items(to_throw)
            if print_progress:
                print(f"Round {i+1} complete.")

    def throw_items(self, to_throw):
        for id,item in to_throw:
            self.monkeys[id].items.append(item)

    def get_common_relief_factor(self):
        return math.prod(monkey.test_divisible for monkey in self.monkeys)

    def get_num_inspections(self):
        return sorted([monkey.num_inspections for monkey in self.monkeys], reverse=True)

    def get_monkey_business_score(self):
        most_active_2 = self.get_num_inspections()[:2]
        return most_active_2[0] * most_active_2[1]
    

if __name__ == "__main__":
    input_path = "input.txt"
    instructions_all = load_txt(input_path)

    # Part 1:
    monkey_sim = Monkey_simulator(instructions_all, relief_method="part1")
    monkey_sim.run_rounds(20, print_progress=False)
    print("Part 1:")
    print(f"Number of inspections: {monkey_sim.get_num_inspections()}")
    print(f"Monkey business score: {monkey_sim.get_monkey_business_score()}")
    print("---------")

    # Part 2:
    monkey_sim2 = Monkey_simulator(instructions_all, relief_method="part2")
    monkey_sim2.run_rounds(10000, print_progress=False)
    print("Part 2:")
    print(f"Number of inspections: {monkey_sim2.get_num_inspections()}")
    print(f"Monkey business score: {monkey_sim2.get_monkey_business_score()}")