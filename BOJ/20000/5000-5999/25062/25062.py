from math import gcd

def divisors(n):
    result = set()
    for x in range(1, int(n ** .5) + 2):
        if n % x == 0:
            result.add(x)
            result.add(n // x)
    
    return result

def solve():
    w, l = map(int, input().split())

    result = {1, 2} | divisors(gcd(w-1, l-1))\
                | divisors(gcd(w-2, l))\
                | divisors(gcd(w, l-2))
    
    print(len(result), *sorted(list(result)))

t = int(input())
for _ in range(t):
    solve()