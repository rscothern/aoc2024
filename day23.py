#!/usr/local/bin/python3

from collections import defaultdict

def read_connections(filename):
    G = defaultdict(set)
    with open(filename, "r") as f:
        for line in f.readlines():
            src, dst = line.strip().split("-")
            if src.startswith("t") or dst.startswith("t"):
                G[src].add(dst)
                G[dst].add(src)

    return G

def bron_kerbosch1(G, r, p, x):
    """
    https://www.dcs.gla.ac.uk/~pat/jchoco/clique/enumeration/tex/report.pdf

    On the first call r and x are set to empty set, and p contains all the vertexes the graph.
    r is the temporary result, p is the set of the possible candidates and x is the excluded set.
    """
    if len(p) + len(x) == 0:
        yield r

    for v in p:
        yield from bron_kerbosch1(G, r | {v}, p & G[v], x & G[v])
        p = p - {v}
        x = x | {v}


G = read_connections("day23ex.txt")

three_len_cliques = [clique for clique in bron_kerbosch1(G, set(), set(G.keys()), set()) if len(clique) == 3]
assert len(three_len_cliques) == 7
