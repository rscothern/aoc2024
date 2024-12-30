#!/usr/local/bin/python3
from __future__ import annotations

from dataclasses import dataclass
from map import Map, Pos
from collections import deque
from typing import Optional

def read_byte_positions(filename, count, dimension):
    m = Map(map=[ ["."] * dimension for i in range(dimension) ])

    with open(filename, "r") as f:
        lines = f.read().splitlines()
        for i, line in enumerate(lines):
            x, y = line.split(",")

            if i == count:
                break

            m.set(Pos(int(x), int(y)), "#")

    return m

@dataclass(frozen=True)
class Node:
    pos: Pos
    pred: Optional[Node]


def shortest_path(map):
    start = Pos(0,0)
    seen = set([start])
    queue = deque([Node(start, None)])

    while queue:
        cur = queue.popleft()

        if cur.pos == Pos(map.width-1, map.height-1):
            steps = 0
            while cur.pred:
                cur = cur.pred
                steps += 1

            return steps

        for offset in cur.pos.adjacent:
            next = cur.pos.add(offset)
            if map.in_map(next) and map.get(next) != "#":
                if next not in seen:
                    seen.add(next)
                    queue.append(Node(pos=next, pred=cur))

    return None

def day18(filename, count, dimension):
    map = read_byte_positions(filename, count, dimension)
    steps = shortest_path(map)
    return steps

def day18_part2(filename, dimension):
    with open(filename, "r") as f:
        map = Map(map=[ ["."] * dimension for i in range(dimension) ])
        for line in f.read().splitlines():
            x, y = line.split(",")
            map.set(Pos(int(x), int(y)), "#")
            steps = shortest_path(map)
            if not steps:
                return x,y

assert day18("day18ex.txt", 12, 7) == 22
assert day18("day18.txt", 1024, 71) == 446

assert day18_part2("day18.txt", 71) == (39,40)
