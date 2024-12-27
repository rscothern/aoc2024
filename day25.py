#!/usr/local/bin/python3

class Key:
    def __init__(self):
        self.vals = [0,0,0,0,0]

    @property
    def pins(self):
        # in favour of more generic parsing, remove the bottom
        # row of pins here
        return [v-1 for v in self.vals]

    def __repr__(self):
        return f"Key({self.pins})"

class Lock:
    def __init__(self):
        self.vals = [0,0,0,0,0]

    @property
    def pins(self):
        return self.vals

    def __repr__(self):
        return f"Lock({self.pins})"


def parse_keys_and_locks(filename):
    current_object = None
    objects = set()
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not current_object and line == "#####":
                current_object = Lock()
            elif not current_object and line == ".....":
                current_object = Key()
            elif not line:
                objects.add(current_object)
                current_object = None
            else:
                for i, symbol in enumerate(line):
                    if symbol == "#":
                        current_object.vals[i] += 1

    objects.add(current_object)
    return objects


def compare(obj1, obj2):
    combination = [sum(p) for p in zip(obj1.pins, obj2.pins)]
    for c in combination:
        if c > 5:
            return False
    return True

def find_matches(filename):
    objects = parse_keys_and_locks(filename)
    keys = list(filter(lambda o: isinstance(o, Key), objects))
    locks = list(filter(lambda o: isinstance(o, Lock), objects))
    return sum(([compare(k, l) for k in keys for l in locks]))


assert find_matches("day25ex.txt") == 3
assert find_matches("day25.txt") == 2824

        
