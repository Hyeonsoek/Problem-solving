import sys

def solve():
    cache = [1, 1]
    for i in range(2, 300):
        cache.append(cache[-1] * 2 + (-1 if i & 1 else 1))
    for input in sys.stdin:
        print(cache[int(input)])

solve()