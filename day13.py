#!/usr/local/bin/python3
from dataclasses import dataclass, field
import re
import sys
from collections import namedtuple

Button = namedtuple("Button", "x y cost")
Prize = namedtuple("Prize", "x y")

@dataclass
class Game:
    button_a: Button = field(default=Button(0, 0, 0))
    button_b: Button = field(default=Button(0, 0, 0))
    prize: Prize = field(default=Prize(0,0))

def parse_input(filename):
    button_re = r"Button ([A|B]): X\+(\d+), Y\+(\d+)"
    prize_re = r"Prize: X=(\d+), Y=(\d+)"
    games = [Game()]
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            m = re.match(button_re, line)
            if m:
                button, x, y = m.group(1), m.group(2), m.group(3)
                if button == "A":
                    games[-1].button_a = Button(int(x), int(y), 3)
                else:
                    games[-1].button_b = Button(int(x), int(y), 1)
            m = re.match(prize_re, line)
            if m:
                x, y = m.group(1), m.group(2)
                games[-1].prize = Prize(int(x), int(y))
                games.append(Game())

    return games


def find_least_cost(button_a, button_b, prize):
    mem = {}
    do_find_least_cost(button_a, button_b, prize, 0, 0, 0, mem, [])
    return mem.get(prize, 0)

def do_find_least_cost(button_a, button_b, prize, cur_x, cur_y, cost, mem, seq):
    if (cur_x, cur_y) == prize:
        #print(f"> found {cur_x=}, {cur_y=}, {cost=}, {seq=}")
        mem[(cur_x, cur_y)] = min(cost, mem.get(cur_x, cur_y), sys.maxsize)
        return cost

    if any([seq.count("A") > 100, seq.count("B") > 100, cur_x > prize.x, cur_y > prize.y]):
        return sys.maxsize

    if (cur_x, cur_y) in mem:
        return mem[(cur_x, cur_y)]

    mem[(cur_x, cur_y)] = cost

    return min([
        do_find_least_cost(button_a, button_b, prize, cur_x + button_a.x, cur_y + button_a.y, cost + button_a.cost, mem, seq+["A"]), 
        do_find_least_cost(button_a, button_b, prize, cur_x + button_b.x, cur_y + button_b.y, cost + button_b.cost, mem, seq+["B"])
    ])


def day13(filename):
    total = 0
    games = parse_input(filename)
    for g in games:
        total += find_least_cost(g.button_a, g.button_b, g.prize)

    return total

assert day13("day13ex.txt") == 480
assert day13("day13.txt") == 37297
