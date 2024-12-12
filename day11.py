#!/usr/local/bin/python3

from collections import defaultdict
from copy import copy

def do_blink(stone_counts):
    current_stones = copy(stone_counts)
    for stone, count in current_stones.items():
        if count == 0:
            continue
        stone_str = f"{stone}"
        if stone == 0:
            stone_counts[0] -= count
            stone_counts[1] += count
        elif len(stone_str) % 2 == 0:
            l = len(stone_str)
            first = int(stone_str[0:int(l/2)])
            second = int(stone_str[int(l/2):])

            stone_counts[first] += count
            stone_counts[second] += count
            stone_counts[stone] -= count
        else:
            stone_counts[int(stone) * 2024] += count
            stone_counts[stone] -= count
    return stone_counts


def blink(stones_str, n):
    stone_counts = defaultdict(int)
    for val in stones_str.split():
        stone_counts[val] = 1

    for i in range(1, n+1):
        stone_counts = do_blink(stone_counts)
        print(i, len(stone_counts))
    return sum(stone_counts.values())

print(blink("125 17", 25))
print(blink("77 515 6779622 6 91370 959685 0 9861", 75))
