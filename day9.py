#!/usr/local/bin/python3

from dataclasses import dataclass


@dataclass
class Node:
    val: str
    id: int

    def __eq__(self, other):
        return self.val == other.val

    @property
    def is_space(self):
        return self.val == "."

    def __repr__(self):
        return self.val
        
SPACE_NODE = Node(".", -1)

def explode(disk_map):
    repr = []
    idx = 0
    for i, num in enumerate(disk_map):
        num = int(num)
        if i % 2 == 0:
            repr.extend([Node(val=str(idx), id=idx)] * num)
            idx += 1
        else:
            repr.extend([SPACE_NODE] * num)

    return repr


def compress(repr):
    first = 0
    last = len(repr) - 1
    while first != last:
        if not repr[first].is_space:
            first += 1
            continue

        repr[first] = repr[last]
        repr[last] = SPACE_NODE
        last -= 1

    return repr


def checksum(accumulated):
    checksum = 0
    for i, val in enumerate(accumulated):
        if not val.is_space:
            checksum += i * val.id

    return checksum

def day9(filename):
    with open(filename, "r") as f:
        input = f.read().strip()
        return checksum(compress(explode(input)))

assert day9("day9ex.txt") == 1928
assert day9("day9.txt") == 6415184586041
