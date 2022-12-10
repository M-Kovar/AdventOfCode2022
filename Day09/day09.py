# Advent of Code 2022
# https://adventofcode.com/2022
# Day 09

class Knot():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.visited_coords = [(x,y)]

    def is_touching(self, other):
        return (abs(self.x - other.x) <= 1) and (abs(self.y - other.y) <= 1)

    def make_step(self, direction):
        if direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        self.update_visited()

    def follow(self, head):
        if not self.is_touching(head):
            # Inferred from the example - don't know why it works, but it works:)
            if abs(self.x - head.x)==1:
                x_new = head.x
            else:
                x_new = sum([self.x, head.x])//2
            # Same for y
            if abs(self.y - head.y)==1:
                y_new = head.y
            else:
                y_new = sum([self.y, head.y])//2
            self.set_coords(x_new, y_new)

    def get_coords(self):
        return self.x, self.y

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        self.update_visited()

    def update_visited(self):
        self.visited_coords.append((self.x, self.y))

    def count_visited(self):
        # Count unique knots only
        return len(set(self.visited_coords))


def load_txt(path):
    with open(path, "r") as file:
        motions = []
        for line in file:
            direction, steps = line.rstrip().split(" ")
            motions.append((direction, int(steps)))
    return motions

def simulate_motions(motions, rope_length=2):
    # Initialize rope
    # (for Part 1, there are only 2 knots: [head,tail])
    knots = [Knot() for _ in range(rope_length)]
    for direction, steps in motions:
        for _ in range(steps):
            for k in range(0,len(knots)-1):
                head = knots[k]
                tail = knots[k+1]
                if k == 0:
                    head.make_step(direction)
                tail.follow(head)
    return knots


if __name__ == "__main__":
    input_path = "input.txt"
    motions = load_txt(input_path)

    # Part 1:
    head, tail = simulate_motions(motions)
    print(f"Part 1: {tail.count_visited()}")

    # Part 2:
    knots = simulate_motions(motions, rope_length=10)
    tail = knots[-1]
    print(f"Part 2: {tail.count_visited()}")