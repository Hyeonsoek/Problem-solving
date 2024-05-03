# N >= M => 0
# N < M
# 10**6 <= 10**7

def solve():
    N, M = map(int, input().split())

    if N >= M:
        print(0)
    else:
        result = 1
        for x in range(1, N + 1):
            result *= (x % M)
            result %= M
        print(result)

solve()