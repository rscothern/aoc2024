#!/usr/local/bin/python3

from enum import Enum

from map import Map, Pos


def load_map(filename):
    map = []
    guard_pos = []
    with open(filename, "r") as f:
        for line in f.readlines():
            map.append(list(line.strip()))
            pos = line.find("^")
            if pos > 0:
                guard_pos.append(Pos(pos, len(map) - 1))

    if len(guard_pos) != 1:
        raise Exception(f"Expected only one guard, got {len(guard_pos)}")

    return Map(map), guard_pos[0]


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def guard_path(map, guard_pos):
    turns = {
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
        next_pos = guard_pos.add(offset)
        if not map.in_map(next_pos):
            break

        if map.get(next_pos) == "#":
            current_direction = turns[current_direction]
        else:
            guard_pos = next_pos
            seen.add(guard_pos)

    return len(seen)


def day6(filename):
    map, guard_pos = load_map(filename)
    return guard_path(map, guard_pos)


assert day6("day6test.txt") == 41
assert day6("day6.txt") == 5029
