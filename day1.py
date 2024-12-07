#!/usr/local/bin/python3

test_1 = [3, 4, 2, 1, 3, 3]
test_2 = [4, 3, 5, 3, 9, 3]

def day1():
    list_1 = []
    list_2 = []
    with open("day1.txt") as f:
        for line in f.readlines():
            a,b = line.strip().split()
            list_1.append(int(a))
            list_2.append(int(b))

    d = sum(abs(a-b) for (a,b) in zip(sorted(list_1), sorted(list_2)))
    return d

print(day1())
