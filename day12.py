#!/usr/local/bin/python3


from map import Pos, Map

def load_map(filename):
    map = []
    with open(filename) as f:
        for _, line in enumerate(f.readlines()):
            line = list(line.strip())
            map.append(line)

    return Map(map)


def explore_areas(map):
    areas = {}
    all = set()
    for pos in map.all_positions:
        plant = map.get(pos)
        if plant not in areas:
            # new plant type
            so_far = []
            do_explore(map, pos, plant, so_far)
            areas[plant] = so_far
            all |= set(so_far)
        else:
            if pos in all:
                # in existing found area
                pass
            else:
                # another area of a previously seen plant
                desc = f"{plant}{pos.x}{pos.y}"
                so_far = []
                do_explore(map, pos, plant, so_far)
                all |= set(so_far)
                areas[desc] = so_far

    return areas


def neighbour_plants(map, pos, plant):
    return [
        p
        for p in [
            Pos(pos.x - 1, pos.y),
            Pos(pos.x + 1, pos.y),
            Pos(pos.x, pos.y - 1),
            Pos(pos.x, pos.y + 1),
        ]
        if map.in_map(p) and map.get(p) == plant
    ]


def do_explore(map, pos, plant, seen):
    cur_plant = map.get(pos)
    if cur_plant != plant:
        return 

    if pos not in seen:
        seen.append(pos)
    else:
        return

    next_pos = neighbour_plants(map, pos, plant)
    for pos in next_pos:
        do_explore(map, pos, plant, seen)


def get_fences(plant_area):
    """
    fences are adjacent non-plant positions
    """
    fences = []
    do_get_fences(plant_area, 0, fences)
    return fences


def do_get_fences(plant_area, idx, fences):
    if idx == len(plant_area):
        return

    current_pos = plant_area[idx]

    for offset in Pos(0,0).adjacent:
        maybe_fence = Pos(current_pos.x + offset.x, current_pos.y + offset.y)
        if maybe_fence not in plant_area:
            fences.append(maybe_fence)

    do_get_fences(plant_area, idx + 1, fences)


def calculate_cost(filename):
    map= load_map(filename)
    areas = explore_areas(map)
    total_cost = 0
    for _, positions in areas.items():
        fences = get_fences(positions)
        cost = len(positions) * len(fences)
        total_cost += cost
    return total_cost


cost = calculate_cost("day12ex.txt")
assert cost == 140
cost = calculate_cost("day12ex2.txt")
assert cost == 1930
cost = calculate_cost("day12.txt")
assert cost == 1477762
