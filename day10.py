#!/usr/local/bin/python3

from collections import namedtuple

Pos = namedtuple("Pos", "x y")

def load_map(filename):
    map = []
    trail_heads = set()
    with open(filename) as f:
        for line in f.readlines():
            map.append(list(line.strip()))
            for pos, lat in enumerate(line):
                if lat == "0":
                    trail_heads.add(Pos(pos, len(map) - 1))

    return map, trail_heads


def score_trails(map, trail_heads):
    total = 0
    for trail_head in trail_heads:
        trails = set()
        do_score_trail(map, trail_head, [], trails)
        total += len(trails)
    return total

def do_score_trail(map, cur, so_far, trails):
    if not all([cur.x >= 0, cur.x < len(map[0]), cur.y >= 0, cur.y < len(map)]):
        return False

    cur_val = int(map[cur.y][cur.x])
    if so_far:
        last = so_far[-1]
        if int(map[last.y][last.x]) + 1 != cur_val:
            return False

    if cur_val == 9:
        trail = (so_far[0], cur)
        trails.add(trail)

        # For part 2, increment every time this point is reached.
        return True

    return any([
        do_score_trail(map, Pos(cur.x-1, cur.y), so_far+[cur], trails),
        do_score_trail(map, Pos(cur.x+1, cur.y), so_far+[cur], trails),
        do_score_trail(map, Pos(cur.x, cur.y+1), so_far+[cur], trails),
        do_score_trail(map, Pos(cur.x, cur.y-1), so_far+[cur], trails)
    ])

map, trail_heads = load_map("day10test.txt")
score = score_trails(map, trail_heads)
assert score == 36

map, trail_heads = load_map("day10.txt")
score = score_trails(map, trail_heads)
assert score == 744
