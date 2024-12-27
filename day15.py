#!/usr/local/bin/python3

from io import UnsupportedOperation
from map import Map, Pos
from copy import copy

class Day15(Map):
    def set(self, pos, val):
        if not self.in_map(pos):
            raise Exception(f"{pos} outside of map")

        self.map[pos.y][pos.x] = val

    def is_wall(self, pos):
        return self.get(pos) == "#"

    def is_box(self, pos):
        return self.get(pos) == "O"

    def is_space(self, pos):
        return self.get(pos) == "."

    def move_box(self, from_pos, to_pos):
        self.set(from_pos, ".")
        self.set(to_pos, "O")

    @property
    def gps_coordinates(self):
        for pos in self.all_positions:
            if self.is_box(pos):
                yield pos.x + 100 * pos.y

def map_and_directions(filename):
    map = []
    directions = []
    robot_pos = Pos(0,0)

    with open(filename, "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if not line:
                continue
            elif line[0] in "<>v^":
                directions.extend(list(line))
            else:
                map.append(list(line))
                for j, loc in enumerate(line):
                    if loc == "@":
                        robot_pos = Pos(j,i)

    m = Day15(map)
    m.set(robot_pos, ".")
    return m, robot_pos, directions


def maybe_move_boxes(map, robot_pos, direction):
    offsets = {
        ">" : Pos(1, 0),
        "<" : Pos(-1, 0),
        "^" : Pos(0, -1),
        "v" : Pos(0, 1)
    }

    reverse_move = {
        ">": True,
        "<": False,
        "^": False,
        "v": True
    }

    next_pos = robot_pos.add(offsets[direction])
    move_robot = False
    if map.is_wall(next_pos):
        pass
    elif map.is_box(next_pos):
        need_move = False
        # find the boxes between here and next gap (if there is one)
        boxes = [next_pos]
        cur = next_pos
        while True:
            cur = cur.add(offsets[direction])
            if map.is_wall(cur):
                break
            elif map.is_box(cur):
                boxes.append(cur)
            elif map.is_space(cur):
                need_move = True
                break

        if need_move:
            move_robot = True
            for box in sorted(boxes, reverse=reverse_move[direction]):
                # move boxes from furthest to nearest to ensure they 
                # don't overwrite each other
                map.move_box(box, box.add(offsets[direction]))
    elif map.is_space(next_pos):
        move_robot = True
    else:
        raise Exception(f"Unexpected map object at {next_pos}")

    return move_robot

def move_robot(map, robot_pos, directions, idx):
    while True:
        if idx == len(directions):
            return True

        next_x, next_y = robot_pos.x, robot_pos.y
        direction = directions[idx]
        if direction == ">":
            next_x += 1 if maybe_move_boxes(map, robot_pos, direction) else 0
        elif direction == "<":
            next_x -= 1 if maybe_move_boxes(map, robot_pos, direction) else 0
        elif direction == "v":
            next_y += 1 if maybe_move_boxes(map, robot_pos, direction) else 0
        elif direction == "^":
            next_y -= 1 if maybe_move_boxes(map, robot_pos, direction) else 0
        else:
            raise UnsupportedOperation()

        robot_pos = Pos(next_x, next_y)
        idx += 1


def day15(filename):
    map, robot_pos, directions = map_and_directions(filename)
    move_robot(map, robot_pos, directions, 0)

    return sum(map.gps_coordinates)

assert day15("day15test.txt") == 2028
assert day15("day15ex.txt") == 10092
assert day15("day15.txt") == 1426855
