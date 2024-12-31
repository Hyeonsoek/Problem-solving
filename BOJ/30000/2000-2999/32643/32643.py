import sys
MAX = 5000001
input = sys.stdin.readline

isprime = [1] * MAX
isprime[0] = 0
for x in range(2, MAX):
    if isprime[x]:
        for xx in range(x * x, MAX, x):
            isprime[xx] = 0

for x in range(2, MAX):
    isprime[x] += isprime[x-1]

def solve():
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        print(isprime[b] - isprime[a-1])

solve()