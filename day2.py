#!/usr/local/bin/python3

test_levels = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

def day2():
            
    def process_level(level) -> bool:
        should_increase = level[1] > level[0]
        last = level[0] - 1 if should_increase else level[0] + 1
        
        for i, num in enumerate(level):
            if abs(num-last) not in [1,2,3]:
                return False
            if num < last and should_increase:
                return False
            if num > last and not should_increase:
                return False

            last = num
            
        return True
        
    levels = []
    with open("day2.txt") as f:
        for line in f.readlines():
            levels.append([int(num) for num in line.split(" ")])

    num_safe = 0
    for level in levels:
        if process_level(level):
            num_safe += 1

    return num_safe

print(day2())
