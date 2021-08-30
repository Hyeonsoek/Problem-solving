import bisect
from itertools import permutations

def solution(n, weak, dist):

    len_weak = len(weak)
    len_dist = len(dist)
    weak = weak + [n+x for x in weak]
    dist = sorted(dist, reverse=True)

    for idx in range(1, len_dist + 1):
        dist_permutate = permutations(dist, idx)

        for p in dist_permutate:
            for i in range(len_weak):
                start = weak[i]
                finish = weak[i + len_weak - 1]

                for j in range(len(p)):
                    start += p[j]
                    if start >= finish:
                        return len(p)
                    start = weak[bisect.bisect_right(weak, start)]
    return -1