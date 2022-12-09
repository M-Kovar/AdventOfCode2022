# Advent of Code 2022
# https://adventofcode.com/2022
# Day 08

import numpy as np

def load_txt(path):
    with open(path, "r") as file:
        grid = []
        for line in file:
            grid.append([int(char) for char in [*line.rstrip()]])
    return grid

def count_visible(vis_grid):
    return sum(sum(vis_grid))

def get_trees_around(tree_grid, tree_row, tree_col):
    trees_around = dict()
    trees_around["right"] = tree_grid[tree_row, tree_col+1:]
    trees_around["bottom"] = tree_grid[tree_row+1:, tree_col]
    # Left and top are reversed to match the order seen by our tree
    trees_around["left"] = tree_grid[tree_row, :tree_col][::-1]
    trees_around["top"] = tree_grid[:tree_row, tree_col][::-1]
    return trees_around

def get_visibility(tree_grid):
    nrows, ncols = tree_grid.shape
    vis_grid = np.full((nrows, ncols), False)    
    for idx_row in range(0,nrows):
        for idx_col in range(0,ncols):
            tree = tree_grid[idx_row, idx_col]
            trees_around = get_trees_around(tree_grid, idx_row, idx_col)
            for tree_row in trees_around.values():
                #  If there are only smaller trees in at least one direction, then it's visible
                if all(tree_row < tree):
                    vis_grid[idx_row, idx_col] = True
                    break
    return vis_grid

def get_scenic_scores(tree_grid):
    nrows, ncols = tree_grid.shape
    score_grid = np.zeros([nrows, ncols], "int")
    for idx_row in range(0,nrows):
        for idx_col in range(0,ncols):
            tree = tree_grid[idx_row, idx_col]
            trees_around = get_trees_around(tree_grid, idx_row, idx_col)
            scenic_score = 1
            for tree_row in trees_around.values():
                # Find distance of the first tree higher than our tree
                blocking_trees = np.where(tree_row >= tree)[0]
                scenic_score *= len(tree_row) if len(blocking_trees)==0 else blocking_trees[0]+1
            score_grid[idx_row, idx_col] = scenic_score
    return score_grid


if __name__ == "__main__":
    input_path = "input.txt"
    trees_raw = load_txt(input_path)
    tree_grid = np.asarray(trees_raw)
    vis_grid = get_visibility(tree_grid)
    
    # Part 1:
    # print(vis_grid)
    print(f"Part 1: {count_visible(vis_grid)}")

    # Part 2:
    score_grid = get_scenic_scores(tree_grid)
    # print(score_grid)
    print(f"Part 2: {np.amax(score_grid)}")