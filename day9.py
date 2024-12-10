#!/usr/local/bin/python3

def explode(disk_map):
    repr = []
    idx = 0
    for i, num in enumerate(disk_map):
        num = int(num)
        if i % 2 == 0:  # id
            repr.extend(f"{idx}" * num)
            idx += 1
        else:
            repr.extend("." * num)

    return repr


def compress(repr):
    first = 0
    last = len(repr) - 1
    while first < last:
        if repr[first] != ".":
            first += 1
            continue

        repr[first] = repr[last]
        last -= 1

    return "".join(repr[0:last])


def checksum(accumulated):
    checksum = 0
    for i, val in enumerate(accumulated):
        checksum += i * int(val)
    return checksum


def compress_and_checksum(data):
    exploded = explode(data)
    compressed = compress(exploded)
    return checksum(compressed)

with open("day9.txt") as f:
    input = f.read()
    input = input.strip()

print(compress_and_checksum(input))
