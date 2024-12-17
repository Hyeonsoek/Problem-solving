import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n = int(input())
    rank = defaultdict(lambda : sys.maxsize)

    for x in range(n):
        a, od, b, *arr = input().split()
        for name in arr:
            rank[name] = min(rank[name], int(b))

    reverse = defaultdict(list)
    for key, value in rank.items():
        reverse[value].append(key)

    count = 1
    items = sorted(reverse.items())
    for i in range(len(items)):
        key, value = items[i]
        if key == count:
            print(key, value[0])
        count += len(value)

solve()