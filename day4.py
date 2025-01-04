#!/usr/local/bin/python3

from map import Map, Pos


def xmas_from_pos(grid, pos):

    def grid_or_none(grid, pos):
        if grid.in_map(pos):
            return grid.get(pos)

        return "."

    found = 0

    offsets = [
        [Pos(1,0), Pos(2,0), Pos(3,0)], # horizontal
        [Pos(1,1), Pos(2,2), Pos(3,3)], # diagonal down
        [Pos(1,-1), Pos(2,-2), Pos(3,-3)], # diagonal up
        [Pos(0,1), Pos(0,2), Pos(0,3)]  # vertical
    ]

    for offset in offsets:
        found += [grid_or_none(grid, pos.add(o)) for o in offset] == list("MAS")
        
    for offset in offsets:
        found += [grid_or_none(grid, pos.subtract(o)) for o in offset] == list("SAM")

    return found


def day4(filename):
    input = ""
    grid = []
    with open(filename, "r") as f:
        input = f.read().splitlines()

    for line in input:
        grid.append(list(line))

    grid = Map(grid)
    total = 0
    for pos in grid.all_positions:
        if grid.get(pos) == "X":
            total += xmas_from_pos(grid, pos)

    return total

assert day4("day4ex.txt") == 18
assert day4("day4.txt") == 2468
