#!/usr/local/bin/python3

from collections import defaultdict, namedtuple

Pos = namedtuple("Pos", "x y")

def read_map(filename):
    map = []
    antennae = defaultdict(list)
    with open(filename) as f:
        for y, line in enumerate(f.readlines()):
            map.append(list(line.strip()))
            for x, l in enumerate(line):
                if l.isalpha() or l.isdigit():
                    antennae[l].append(Pos(x, y))

    return map, antennae

def find_antinodes(map, antennae):
    def in_map(map, pos):
        in_map = all(
            [
                pos.x >= 0,
                pos.x < len(map[0]),
                pos.y >= 0,
                pos.y < len(map),
            ]
        )
        print(f"{in_map}? for {pos}")
        return in_map


    all_positions = set()
    for a, positions in antennae.items():
        num = len(positions)
        if num == 1:
            continue
        for i in range(num):
            for j in range(num):
                if i != j:
                    pos1 = positions[i]
                    pos2 = positions[j]
                    offset = Pos(pos2.x - pos1.x, pos2.y - pos1.y)
                    an1 = pos1
                    while in_map(map, an1):
                        all_positions.add(an1)
                        pos1 = an1
                        an1 = Pos(pos1.x - offset.x, pos1.y - offset.y)

                    an2 = pos2
                    while in_map(map, an2):
                        all_positions.add(an2)
                        pos2 = an2
                        an2 = Pos(pos2.x + offset.x, pos2.y + offset.y)

    return all_positions

map, antennae = read_map("day8test.txt")
antinodes = find_antinodes(map, antennae)
assert len(antinodes) == 34, f"expected 34, got {len(antinodes)}"

map, antennae = read_map("day8.txt")
antinodes = find_antinodes(map, antennae)
assert len(antinodes) == 861, f"expected 861, got {len(antinodes)}"
