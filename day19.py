#!/usr/local/bin/python3

def parse_input(filename):
    patterns = set()
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        towels = lines[0].split(", ")
        patterns = {line for line in lines[2:]}

    return frozenset(towels), patterns


def is_arrangable(towels, design, mem):
    if design == "":
        return True

    for i in range(len(design)):
        pattern = design[:i+1]
        if pattern in towels:
            rest = design[len(pattern):]
            if rest not in mem:
                mem[rest] = is_arrangable(towels, rest, mem)
            success = mem[rest]
            if success:
                return True

    return False

def day19(filename):
    towels, patterns = parse_input(filename)
    total = 0
    for pattern in patterns:
        mem = {}
        found = is_arrangable(towels, pattern, mem)
        print(mem)
        total += int(found)
    return total

assert day19("day19ex.txt") == 6
assert day19("day19.txt") == 308
