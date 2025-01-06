from bisect import *

def solve():
    n, score, p = map(int, input().split())

    if n == 0:
        return 1

    arr = sorted(list(map(lambda x:-int(x), input().split())))
    left = bisect_left(arr, -score) + 1
    right = bisect_right(arr, -score) + 1
    return left if right <= p else -1

print(solve())