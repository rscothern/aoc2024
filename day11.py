#!/usr/local/bin/python3

def do_blink(input):
    transformed = []
    for stone in input:
        if stone == "0":
            transformed.append("1")
        elif len(stone) % 2 == 0:
            l = len(stone)
            first = stone[0:int(l/2)]
            second = stone[int(l/2):]
            transformed.extend([f"{int(first)}", f"{int(second)}"])
        else:
            stone = int(stone) * 2024
            transformed.append(f"{stone}")
    return transformed


def blink(stones, n):
    print(f"{stones=}")
    for i in range(1, n+1):
        stones = do_blink(stones)
        print(i, len(stones))
    return len(stones)

print(blink("77 515 6779622 6 91370 959685 0 9861".split(" "), 25))
