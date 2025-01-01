#!/usr/local/bin/python3
from __future__ import annotations

from dataclasses import dataclass
from map import Map, Pos
from collections import deque
from typing import Optional

def load_map(filename):
    map = []
    start_pos = end_pos = None
    with open(filename) as f:
        for y, line in enumerate(f.readlines()):
            map.append(list(line.strip()))
            for x, char in enumerate(line):
                if char == "S":
                    start_pos = Pos(x, y)
                if char == "E":
                    end_pos = Pos(x , y)

    return Map(map), start_pos, end_pos

@dataclass(frozen=True)
class Node:
    pos: Pos
    pred: Optional[Node]


def shortest_path(map, start, end):
    seen = set([start])
    queue = deque([Node(start, None)])

    while queue:
        cur = queue.popleft()

        if cur.pos == end:
            path = []
            while cur:
                path.append(cur.pos)
                cur = cur.pred
            path.reverse()
            return path

        for offset in cur.pos.adjacent:
            next = cur.pos.add(offset)
            if map.in_map(next) and map.get(next) != "#":
                if next not in seen:
                    seen.add(next)
                    queue.append(Node(pos=next, pred=cur))

    return []

def day20(filename, threshold):
    """
    Find the shortest path, look for positions separated by a wall, and
    find the saving by ignoring it
    """
    map, start, end = load_map(filename)
    shortcuts = 0

    path = shortest_path(map, start, end)
    path_lookup = { pos: i for i, pos in enumerate(path) }

    for i in range(len(path)):
        from_pos = path[i]
        horiz_jump = from_pos.add(Pos(2,0))
        if horiz_jump in path_lookup and map.get(from_pos.add(Pos(1,0))) == "#":
            saving = abs(path_lookup[horiz_jump] - i) - 2
            if saving >= threshold:
                shortcuts += 1
        
        vert_jump = from_pos.add(Pos(0, 2))
        if vert_jump in path_lookup and map.get(from_pos.add(Pos(0,1))) == "#":
            saving = abs(path_lookup[vert_jump] - i) - 2
            if saving >= threshold:
                shortcuts += 1
        
    return shortcuts

    
assert day20("day20ex.txt", 0) == 44
assert day20("day20.txt", 100) == 1502
