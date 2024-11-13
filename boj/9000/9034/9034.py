import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    length = n + m + 1
    tree = [0] * length
    
    def update(x, v):
        while x <= length:
            tree[x] += v
            x += x & -x
    
    def query(x):
        r = 0
        while 0 < x:
            r += tree[x]
            x -= x & -x
        return r

    queries = []
    values = set([0])
    coords = defaultdict(int)
    for x in range(m):
        q, *a = input().split()
        if q == 'R':
            index, value = map(int, a)
            coords[index] += value
            values.add(coords[index])
            queries.append((q, index, value))
        else:
            index = int(a[0])
            queries.append((q, index))

    values = sorted(values, reverse=True)
    indexes = defaultdict(int)
    for i, x in enumerate(values):
        indexes[x] = i + 1

    trace = defaultdict(int)
    for x in range(m):
        if queries[x][0] == 'R':
            q, i, v = queries[x]
            if trace[i] > 0:
                update(indexes[trace[i]], -1)
            trace[i] += v
            update(indexes[trace[i]], 1)
        else:
            q, i = queries[x]
            print(query(indexes[trace[i]]-1) + 1)

for _ in range(int(input())):
    solve()