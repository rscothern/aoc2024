#!/usr/local/bin/python3

def day1():
    a = [2, 5, 3, 7]
    b = [9, 4, 11, 2]

    d = sum(a+b for (a,b) in zip(sorted(a), sorted(b)))
    print("distance: ", d)

day1()
