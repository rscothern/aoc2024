from collections import namedtuple
from dataclasses import dataclass
from typing import List


PosType = namedtuple("Pos", "x y")


class Pos(PosType):
    @property
    def adjacent(self):
        for offset in [Pos(-1, 0), Pos(1, 0), Pos(0, -1), Pos(0, 1)]:
            yield offset

    def add(self, other):
        return Pos(self.x + other.x, self.y + other.y)



@dataclass
class Map:
    map: List[List[str]]

    @property
    def width(self):
        return len(self.map[0])

    @property
    def height(self):
        return len(self.map)

    def get(self, pos):
        if not self.in_map(pos):
            raise Exception(f"{pos} outside of map")

        return self.map[pos.y][pos.x]

    def in_map(self, pos):
        return all(
            [
                pos.x >= 0,
                pos.x < self.width,
                pos.y >= 0,
                pos.y < self.height,
            ]
        )

    @property
    def all_positions(self):
        for x in range(self.width):
            for y in range(self.height):
                yield Pos(x, y)

    def draw(self, positions={}):
        print(f"Map: {self.width} x {self.height}")
        for y in range(self.height):
            for x in range(self.width):
                pos = Pos(x, y)
                if pos in positions:
                    print(positions[pos], end=" ")
                else:
                    print(self.get(pos), end=" ")
            print()
