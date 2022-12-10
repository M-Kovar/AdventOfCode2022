# Advent of Code 2022
# https://adventofcode.com/2022
# Day 10

def load_txt(path):
    with open(path, "r") as file:
        input_list = [line.rstrip() for line in file]
    return input_list

def get_register_values(instructions):
    register = [x := 1]
    for instr in instructions:
        if "noop" in instr:
            register.append(x)
        elif "addx" in instr:
            _, value = instr.split(" ")
            register.append(x)
            x += int(value)
            register.append(x)
    return register
            
def get_signal_strength(register_values, at_indices):
    return [idx*val for idx,val in enumerate(register_values, start=1) if idx in at_indices]

def render_image(register, width=40, enhance_readability=False):
    lit  = "█" if enhance_readability else "#"
    dark = " " if enhance_readability else "."
    row  = []
    for idx,spr_pos in enumerate(register, start=0):
        idx_inrow = idx - (idx//width)*width
        pixel = lit if (idx_inrow in range(spr_pos-1,spr_pos+2)) else dark
        row.append(pixel)
        if idx_inrow == width-1:
            print("".join(row))
            row = []
    return

if __name__ == "__main__":
    input_path = "input.txt"
    instructions = load_txt(input_path)
    register = get_register_values(instructions)
    signal_strength = get_signal_strength(register, at_indices=range(20,220+1,40))

    # Part 1:
    print(f"Part 1: {sum(signal_strength)}")

    # Part 2:
    print("Part 2:")
    render_image(register, enhance_readability=True)