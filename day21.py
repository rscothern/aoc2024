#!/usr/local/bin/python3
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Optional

from map import Map, Pos


@dataclass(frozen=True)
class Node:
    pos: Pos
    pred: Optional[Node]


class Keypad:
    DIRECTIONS = {
        Pos(-1, 0): "<",
        Pos(1, 0): ">",
        Pos(0, -1): "^",
        Pos(0, 1): "v",
    }

    def __init__(self, keys):
        map = Map(keys)
        self.positions = {map.get(key_pos): key_pos for key_pos in map.all_positions}
        self.map = map
        self.pos = self.positions["A"]

    def _shortest_path(self, end):
        seen = set([self.pos])
        queue = deque([Node(self.pos, None)])

        while queue:
            cur = queue.popleft()

            if cur.pos == end:
                seq = []
                while cur:
                    seq.append(cur.pos)
                    cur = cur.pred
                self.pos = end
                seq.reverse()
                return seq

            for offset in cur.pos.adjacent:
                next = cur.pos.add(offset)
                if self.map.in_map(next) and self.map.get(next) != "#":
                    if next not in seen:
                        seen.add(next)
                        queue.append(Node(pos=next, pred=cur))
        return []

    def _path_to(self, symbol):
        return self._shortest_path(self.positions[symbol])

    def keypresses_for_code(self, code):
        SORT_ORDER = {"^": 0, ">": 0, "v": 1, "<": 2}

        directions = []
        for symbol in code:
            path = self._path_to(symbol)
            sub_path = []
            for i in range(len(path) - 1):
                x = path[i + 1].subtract(path[i])
                sub_path.append(Keypad.DIRECTIONS[x])

            sub_path.sort(key=lambda v: SORT_ORDER[v])
            sub_path.append("A")
            directions.append(sub_path)

        return directions


class NumericKeypad(Keypad):
    def __init__(self):
        keys = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]

        super().__init__(keys)


class DirectionalKeypad(Keypad):
    def __init__(self):
        keys = [
            ["#", "^", "A"],
            ["<", "v", ">"],
        ]
        super().__init__(keys)


def flatten(items, seqtypes=(list, tuple)):
    for i, _ in enumerate(items):
        while i < len(items) and isinstance(items[i], seqtypes):
            items[i : i + 1] = items[i]
    return items


def key_presses(d, keypresses):
    all = []
    for k in keypresses:
        keypresses = d.keypresses_for_code(k)
        all.extend(keypresses)

    flatten(all)
    return all


def day21(filename):
    with open(filename, "r") as f:
        total = 0
        for code in f.read().splitlines():
            k = NumericKeypad()
            keypresses = flatten(k.keypresses_for_code(code))
            keypresses = key_presses(DirectionalKeypad(), keypresses)
            keypresses = key_presses(DirectionalKeypad(), keypresses)

            print(code, "".join(keypresses), len(keypresses))
            total += int(code[:3]) * len(keypresses)

        return total


assert day21("day21ex.txt") == 126384
