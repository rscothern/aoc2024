#!/usr/local/bin/python3

from collections import defaultdict

from map import Map, Pos


def read_map(filename):
    map = []
    antennae = defaultdict(list)
    with open(filename, "r") as f:
        for y, line in enumerate(f.readlines()):
            map.append(list(line.strip()))
            for x, l in enumerate(line):
                if l.isalpha() or l.isdigit():
                    antennae[l].append(Pos(x, y))

    return Map(map), antennae


def find_antinodes(map, antennae):
    all_positions = set()
    for _, positions in antennae.items():
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
                    while map.in_map(an1):
                        all_positions.add(an1)
                        pos1 = an1
                        an1 = Pos(pos1.x - offset.x, pos1.y - offset.y)

                    an2 = pos2
                    while map.in_map(an2):
                        all_positions.add(an2)
                        pos2 = an2
                        an2 = Pos(pos2.x + offset.x, pos2.y + offset.y)

    return all_positions


def day8(filename):
    map, antennae = read_map(filename)
    antinodes = find_antinodes(map, antennae)
    return len(antinodes)


assert day8("day8test.txt") == 34
assert day8("day8.txt") == 861
