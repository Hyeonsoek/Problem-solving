import sys
input = sys.stdin.readline

t, w = map(int, input().split())
tree = [int(input()) for _ in range(t)]
cache = [[[-1] * 2 for _ in range(w+1)] for _ in range(t+1)]

def dp(time, count, loc):
    if time >= t:
        return 0

    if cache[time][count][loc] != -1:
        return cache[time][count][loc]

    result = dp(time + 1, count, loc) + (loc == (tree[time]-1))
    if count < w:
        result = max(result, dp(time + 1, count + 1, not loc) + (not loc == tree[time]-1))

    cache[time][count][loc] = result
    return result


print(dp(0, 0, 0))