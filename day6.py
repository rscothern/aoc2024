#!/usr/local/bin/python3

from collections import namedtuple
from enum import Enum

Pos = namedtuple("Pos", "x y")


def load_map(filename):
    map = []
    guard_pos = []
    with open(filename) as f:
        for line in f.readlines():
            map.append(list(line.strip()))
            pos = line.find("^")
            if pos > 0:
                guard_pos.append(Pos(pos, len(map) - 1))

    if len(guard_pos) != 1:
        raise Exception(f"Expected only one guard, got {len(guard_pos)}")
    guard_pos = guard_pos[0]

    if map[guard_pos.y][guard_pos.x] != "^":
        raise Exception("Unexpected guard symbol")

    return map, guard_pos


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def guard_path(map, guard_pos):
    def in_map(map, guard_pos):
        in_map = all(
            [
                guard_pos.x >= 0,
                guard_pos.x < len(map),
                guard_pos.y >= 0,
                guard_pos.y < len(map[0]),
            ]
        )
        return in_map

    next_direction = {
        Direction.UP: Direction.RIGHT,
        Direction.RIGHT: Direction.DOWN,
        Direction.DOWN: Direction.LEFT,
        Direction.LEFT: Direction.UP,
    }

    moves = {
        Direction.UP: Pos(0, -1),
        Direction.DOWN: Pos(0, 1),
        Direction.LEFT: Pos(-1, 0),
        Direction.RIGHT: Pos(1, 0),
    }

    current_direction = Direction.UP
    seen = set()
    while True:
        offset = moves[current_direction]
        next_pos = Pos(guard_pos.x + offset.x, guard_pos.y + offset.y)
        if not in_map(map, next_pos):
            break

        if map[next_pos.y][next_pos.x] == "#":
            # print(
            #     f"change direction {current_direction} => {next_direction[current_direction]}, {len(seen)=}"
            # )
            current_direction = next_direction[current_direction]
        else:
            guard_pos = next_pos
            seen.add(guard_pos)

    return len(seen)


map, guard_pos = load_map("day6test.txt")
for row in map:
    print(row)
print("Guard", guard_pos, map[guard_pos.y][guard_pos.x])

moves = guard_path(map, guard_pos)
assert moves == 41, f"Test should produce 41 moves, got {moves}"
print(moves)

m, guard_pos = load_map("day6.txt")
moves = guard_path(m, guard_pos)
print(moves)
