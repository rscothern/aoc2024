#!/usr/local/bin/python3
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional
from heapq import heappop, heappush

from map import Map, Pos


def load_map(filename):
    map = []
    start_pos = None
    with open(filename) as f:
        for y, line in enumerate(f.readlines()):
            map.append(line.strip())
            for x, char in enumerate(line):
                if char == "S":
                    start_pos = Pos(x, y)

    return Map(map), start_pos


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

get_direction = {
    Pos(0, -1): Direction.NORTH,
    Pos(1, 0): Direction.EAST,
    Pos(0, 1): Direction.SOUTH,
    Pos(-1, 0): Direction.WEST,
}

@dataclass(frozen=True)
class Node:
    pos: Pos
    pred: Optional[Node]
    score: int
    direction: Direction

    def __eq__(self, other):
        return self.pos == other.pos

    def __repr__(self):
        if self.pred is None:
            pred_str = "None"
        else:
            pred_str = f"{self.pred.pos}"
        return f"Node(pos={self.pos}, pred={pred_str}, score={self.score}, direction={self.direction})"

    def __lt__(self, other):
        return self.score < other.score

    def __hash__(self):
        return hash(self.pos)

def already_seen(pos, seen):
    for p in seen:
        if p.pos == pos:
            return p.score
    return None


def best_path(map, start_pos):
    """
    Dijkstra's algorithm with turn cost as weights
    """
    seen = set()

    pq = [Node(start_pos, None, 0, Direction.EAST)]
    while pq:
        cur = heappop(pq)
        if map.get(cur.pos) == "E":
            path = []
            node = cur.pred
            while node:
                path.append(node.pos)
                node = node.pred
            return cur.score, path

        for adj in cur.pos.adjacent:
            next_pos = cur.pos.add(adj)
            next_direction = get_direction[adj]

            score_adj = 1
            if next_direction != cur.direction:
                score_adj += 1000

            new_score = cur.score + score_adj
            new_pred = cur

            seen_score = already_seen(next_pos, seen)
            if seen_score:
                adjusted_score = cur.score + score_adj
                if seen_score > adjusted_score:
                    new_score = adjusted_score
                    new_pred = adj
                continue

            if map.get(next_pos) == "#":
                continue

            next_node = Node(next_pos, new_pred, new_score, next_direction)
            seen.add(next_node)
            heappush(pq, next_node)

    return score


map, start_pos = load_map("day16ex.txt")
score, path = best_path(map, start_pos)
map.draw(path)

map, start_pos = load_map("day16.txt")
score, path = best_path(map, start_pos)
assert score == 109516
