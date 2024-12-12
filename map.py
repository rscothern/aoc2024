from collections import namedtuple
from dataclasses import dataclass
from typing import List


PosType = namedtuple("Pos", "x y")
class Pos(PosType):
    @property
    def adjacent(self):
        for offset in [Pos(-1, 0), Pos(1, 0), Pos(0, -1), Pos(0, 1)]:
            yield offset

@dataclass
class Map():
    map: List[List[int]]

    @property
    def width(self):
        return len(self.map[0])

    @property
    def height(self):
        return len(self.map)

    def get(self, pos):
        return self.map[pos.y][pos.x]

    def in_map(self, pos):
        return all(
            [
                pos.x >= 0,
                pos.x < self.width,
                pos.y >= 0,
                pos.y < self.height,
            ])

    @property
    def all_positions(self):
        for x in range(self.width):
            for y in range(self.height):
             yield Pos(x, y)
