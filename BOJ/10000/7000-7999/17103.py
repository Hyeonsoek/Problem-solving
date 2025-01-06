import sys
input = sys.stdin.readline

MAX = 1000001
isprime = [1] * MAX
for x in range(2, MAX):
    if isprime[x]:
        for xx in range(x*x, MAX, x):
            isprime[xx] = 0
isprime[0] = 0
isprime[1] = 0
            
prime = []
for x in range(2, MAX):
    if isprime[x]:
        prime.append(x)

def solve():
    result = 0
    n = int(input())
    for x in range(len(prime)):
        if prime[x] > n // 2:
            break
        
        if n > prime[x] and isprime[n - prime[x]]:
            result += 1
        
    print(result)

for x in range(int(input())):
    solve()