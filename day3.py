#!/usr/local/bin/python3
import re

test_mem = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def day3(filename):
    with open("day3.txt", "r") as f:
        mem = f.read()

    pattern = r"mul\((\d+),(\d+)\)"
    prog = re.compile(pattern)
    matches = prog.finditer(mem)
    total = 0
    for m in matches:
        x, y = m.group(1, 2)
        total += int(x) * int(y)

    return total


assert day3("day3.txt") == 192767529
