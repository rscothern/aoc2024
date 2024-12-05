#!/usr/local/bin/python3

def xmas_from_pos(grid, x, y):

    def grid_or_none(grid, x, y):
        if x < 0 or x >= len(grid):
            return "."
        if y < 0 or y>= len(grid[0]):
            return "."
        return grid[x][y]
    
    MAS = "MAS"
    found = 0

    # forward horizontal
    if MAS == grid_or_none(grid,x+1,y) + grid_or_none(grid,x+2,y) + grid_or_none(grid,x+3,y):
        found += 1

    # forward vertical
    if MAS == grid_or_none(grid,x,y+1) + grid_or_none(grid,x,y+2) + grid_or_none(grid,x,y+3):
        found += 1

    # backwards horizontal
    if MAS == grid_or_none(grid,x,y-1) + grid_or_none(grid,x,y-2) + grid_or_none(grid,x,y-3):
        found  += 1
        
    # backwards vertical
    if MAS == grid_or_none(grid,x-1,y) + grid_or_none(grid,x-2,y) + grid_or_none(grid,x-3,y):
        found += 1

    # forward diagonal down
    if MAS == grid_or_none(grid,x+1,y+1) + grid_or_none(grid,x+2,y+2) + grid_or_none(grid,x+3,y+3):
        found += 1

    # forward diagonal up
    if MAS == grid_or_none(grid,x-1,y-1) + grid_or_none(grid,x-2,y-2) + grid_or_none(grid,x-3,y-3):
        found += 1

    # backwards diagonal up
    if MAS == grid_or_none(grid,x+1,y-1) + grid_or_none(grid,x+2,y-2) + grid_or_none(grid,x+3,y-3):
        found += 1

    # backwards diagonal up
    if MAS == grid_or_none(grid,x-1,y+1) + grid_or_none(grid,x-2,y+2) + grid_or_none(grid,x-3,y+3):
        found += 1

    return found
    
    
def day4():
    test_input ="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    input = ""
    grid = []
    with open("day4.txt") as f:
        input = f.read().strip()

    for line in input.split("\n"):
        grid.append(list(line))

    total = 0
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            if grid[x][y] == "X":
                total += xmas_from_pos(grid,x,y)
    print(f"Total XMAS = {total}")

day4()
