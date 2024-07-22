def solve():
    n = int(input())
    
    result = 0
    isprime = [False] * (n + 1)
    for x in range(2, n + 1):
        if not isprime[x]:
            isprime[x] = True
            result += x
            for xx in range(x * x, n + 1, x):
                if not isprime[xx]:
                    isprime[xx] = True
                    result += x
            
    print(result)

solve()