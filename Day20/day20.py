# Advent of Code 2022
# https://adventofcode.com/2022
# Day 20

def load_txt(path):
    with open(path, "r") as file:
        input_list = [int(line.rstrip()) for line in file]
    return input_list

class CircularList:

    def __init__(self, num_list, decryption_key=1):
        self.num_list = num_list
        self.decryption_key = decryption_key

    def mix(self, times=1):
        num_list = [num*self.decryption_key for num in self.num_list]
        ln = len(num_list)
        positions = list(range(ln))
        # Repeat multiple times for part 2
        for _ in range(times):
            for i in range(ln):
                position = positions.index(i)
                value = num_list[position]
                position_new = (position + value) % (ln-1)
                # Pop from old position and insert it to a new one
                num_list.insert(position_new, num_list.pop(position))
                positions.insert(position_new, positions.pop(position))
        self.num_list_decrypted = num_list
        return self.num_list_decrypted

    def get_grove_coordinates(self, significant_positions=[1000, 2000, 3000], after_value=0):
        coord_pos = [(sig + self.num_list_decrypted.index(after_value)) % len(self.num_list_decrypted) for sig in significant_positions]
        return [self.num_list_decrypted[p] for p in coord_pos]


if __name__ == "__main__":
    input_path = "input.txt"
    num_list = load_txt(input_path)

    # Part 1:
    clist1 = CircularList(num_list)
    clist1.mix()
    print(f"Part 1: {sum(clist1.get_grove_coordinates())}")

    # Part 2:
    clist2 = CircularList(num_list, decryption_key=811589153)
    clist2.mix(times=10)
    print(f"Part 2: {sum(clist2.get_grove_coordinates())}")