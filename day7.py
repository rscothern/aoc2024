#!/usr/local/bin/python3

def find_operators(filename):
    total = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            tokens = line.split(":")
            target = int(tokens[0])
            operands = [int(num) for num in tokens[1].split()]
            if do_find_operators(target, operands[0], operands[1:], [operands[0]]):
                total += target

    return total

def do_find_operators(target, so_far, rem, equation):
    if len(rem) == 0:
        if target == so_far:
            print(f"Success: {target=}, {equation=}")
            return True
        else:
            return False

    return any([
        do_find_operators(target, so_far+rem[0], rem[1:], equation + ["+", rem[0]]),
        do_find_operators(target, so_far*rem[0], rem[1:], equation + ["*", rem[0]]),
        do_find_operators(target, int(f"{so_far}{rem[0]}"), rem[1:], equation + ["||", rem[0]])
    ])


def check(filename, expected):
    res = find_operators(filename)
    print(f"Got {res} for {filename}")


check("day7test.txt", 3749)
check("day7.txt", 945512582195)
