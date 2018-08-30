# The power set of a set is the set of all its subsets.
# Write a function that, given a set, generates its power set.
# For example, given the set {1, 2, 3},
# it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

import math


def power_set(inp, inp_size):
    pow_set_size = int(math.pow(2, inp_size))
    out = set()
    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        temp = []
        for j in range(0, inp_size):
            if (counter & (1 << j)) > 0:
                temp.append(inp[j])
        out.add(''.join(map(str, temp)))
    return out


if __name__ == "__main__":
    inp = [1, 2, 3]
    print "Power set:", power_set(inp, len(inp))
