import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        m = int(input())

        cache = [0] * (m + 1)

        for x in range(n):
            if m >= a[x]:
                cache[a[x]] += 1
                for amount in range(m+1):
                    if amount >= a[x]:
                        cache[amount] += cache[amount - a[x]]

        print(cache[m])

solve()