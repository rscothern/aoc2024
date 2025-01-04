#!/usr/local/bin/python3


def do_find_operators(target, so_far, rem, equation):
    if len(rem) == 0:
        return target == so_far

    return any(
        [
            do_find_operators(
                target, so_far + rem[0], rem[1:], equation + ["+", rem[0]]
            ),
            do_find_operators(
                target, so_far * rem[0], rem[1:], equation + ["*", rem[0]]
            ),
            do_find_operators(
                target, int(f"{so_far}{rem[0]}"), rem[1:], equation + ["||", rem[0]]
            ),
        ]
    )


def day7(filename):
    total = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            tokens = line.split(":")
            target = int(tokens[0])
            operands = [int(num) for num in tokens[1].split()]
            if do_find_operators(target, operands[0], operands[1:], [operands[0]]):
                total += target

    return total


assert day7("day7test.txt") == 11387
assert day7("day7.txt") == 271691107779347
