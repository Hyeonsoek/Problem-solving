import sys
sys.setrecursionlimit(2000000)
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
cache = [-1] * (n+1)
cache[n] = 0

def dp(day):
    if cache[day] != -1:
        return cache[day]

    result = 0
    if day + 1 <= n:
        result = max(result, dp(day+1))

    if day + arr[day][0] <= n:
        case2 = dp(day + arr[day][0]) + arr[day][1]
        result = max(result, case2)

    cache[day] = result
    return cache[day]

print(dp(0))