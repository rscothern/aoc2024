#!/usr/local/bin/python3
from copy import copy
from io import UnsupportedOperation

def build_map(filename):
    input = {}
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            if ":" in line:
                wire, val = line.split(":")
                input[wire] = int(val)
            elif "->" in line:
                tokens = line.split()
                wire_in_1, operand, wire_in_2, wire_out = tokens[0], tokens[1], tokens[2], tokens[4]
                input[wire_out] = [wire_in_1, operand, wire_in_2]
            else:
                pass
    return input

def calculate(op1, operand, op2):
    res = 0
    if operand == "XOR":
        res = op1 ^ op2
    elif operand == "AND":
        res = op1 & op2
    elif operand == "OR":
        res = op1 | op2
    else:
        raise UnsupportedOperation(operand)
    return res


def flatten(input):
    needs_flatten = False
    flattened = copy(input)
    for k, v in input.items():
        if isinstance(v, int):
            continue
        else:
            needs_flatten = True
            op1, operand, op2 = v[0], v[1], v[2]

            if op1 in flattened and isinstance(flattened[op1], int):
                op1 = flattened[op1]
            if op2 in flattened and isinstance(flattened[op2], int):
                op2 = flattened[op2]

            if isinstance(op1, int) and isinstance(op2, int):
                flattened[k] = calculate(op1, operand, op2)
            else:
                flattened[k] = [op1, operand, op2]

    return flattened, needs_flatten


def day24(filename):
    input = build_map(filename)

    flattened, needs_flatten = flatten(input)
    while needs_flatten:
        flattened, needs_flatten = flatten(flattened)

    output = "".join([str(flattened[k]) for k in sorted(flattened.keys(), reverse=True) if k.startswith("z")])
    return int(output, 2)

assert day24("day24ex.txt") == 2024
assert day24("day24.txt") == 60614602965288
