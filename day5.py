#!/usr/local/bin/python3

from collections import defaultdict

# directed graph representing page order dependencies
G = defaultdict(set)


def process_file(filename):
    middles = []
    with open("day5.txt") as f:
        for line in f.readlines():
            if "|" in line:
                f, t = line.strip().split("|")
                G[f].add(t)
            elif "," in line:
                page_list = line.strip().split(",")
                if check_page_order(page_list):
                    if len(page_list) % 2 == 0:
                        raise Exception(f"Cannot take middle of even number: {page_list}")
                    middle_pos = int(len(page_list)/2)
                    middles.append(int(page_list[middle_pos]))

    return middles

def check_page_order(pages):
    """
    If we can find a path through the graph of all pages
    in order then the ordering is valid
    """

    if len(pages) == 1:
        return True

    cur = pages[0]
    next = pages[1]
    if next not in G[cur]:
        return False

    return check_page_order(pages[1:])

middles = process_file("day5.txt")
print(sum(middles))
        
