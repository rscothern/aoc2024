#!/usr/local/bin/python3

def day2():
    levels = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]

    def process_level(level) -> bool:
        should_increase = level[1] > level[0]
        last = level[0] - 1
        for i, num in enumerate(level):
            if abs(num-last) not in [1,2,3]:
                print(f"Level bad, delta too large: {num-last=}, {level=}")
                return False
            if level[1] < level[0] and should_increase:
                print(f"Level bad, {should_increase=}: {level=}")
                return False
            if level[1] > level[0] and not should_increase:
                print(f"Level bad, {should_increase=}: {level=}")
                return False

            last = num
            
        print(f"Level ok {level=}")
        return True
        
    for level in levels:
        print(f"Processing {level}")
        process_level(level)

day2()
