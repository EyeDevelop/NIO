import string
import itertools
from collections import OrderedDict

n = int(input())
mapper = OrderedDict()

for i in range(n):
    r = list(input())

    if string.ascii_uppercase[i] not in mapper.keys():
        mapper[string.ascii_uppercase[i]] = OrderedDict()

    for l in range(len(r)):
        if l == i:
            mapper[string.ascii_uppercase[i]][string.ascii_uppercase[i]] = 0
            continue

        if r[l] == "1":
            mapper[string.ascii_uppercase[i]][string.ascii_uppercase[l]] = 1
        elif r[l] == "0":
            mapper[string.ascii_uppercase[i]][string.ascii_uppercase[l]] = 1000000


# O(n!)         -- INSUFFICIENT
def brute_force(dists_dict):
    for combo in itertools.permutations(dists_dict.keys()):
        failed = False
        next_letters = list(combo)

        for letter in combo:
            if letter in next_letters:
                next_letters = dists_dict[letter]
            else:
                failed = True
                break

        if failed:
            continue
        else:
            print("".join(combo))
            break


# O(n^2 2^n)    -- INSUFFICIENT
def held_karp(dists):
    """
    Implementation of Held-Karp, an algorithm that solves the Traveling
    Salesman Problem using dynamic programming with memoization.
    Parameters:
        dists: distance matrix
    Returns:
        A tuple, (cost, path).
    """
    n = len(dists)

    # Maps each subset of the nodes to the cost to reach that subset, as well
    # as what node it passed before reaching this subset.
    # Node subsets are represented as set bits.
    C = {}

    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    # We're interested in all bits but the least significant (the start state)
    bits = (2 ** n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    # Add implicit start state
    path.append(0)

    return opt, list(reversed(path))


dists = []
for key in mapper.keys():
    dists.append(list(mapper[key].values()))

res = held_karp(dists)

path = "".join([string.ascii_uppercase[x] for x in res[1]])
print(path)
