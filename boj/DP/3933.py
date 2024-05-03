import sys
input = sys.stdin.readline

def solve():
    MAX = 1 + (1 << 15)
    dp = [[0] * 5 for _ in range(MAX)]

    for x in range(1, int(MAX ** 0.5) + 1):
        dp[x*x][1] += 1

        for y in range(x*x, MAX):
            for k in range(2, 5):
                dp[y][k] += dp[y - x*x][k-1]

    while True:
        n = int(input())
        if n == 0:
            break
        print(sum(dp[n]))

solve()