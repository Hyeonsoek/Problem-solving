def solve():
    n, k = int(input()), int(input())

    isprime = [1] * 100001
    for x in range(2, 100001):
        if isprime[x]:
            for xx in range(x*x, 100001, x):
                isprime[xx] = 0

    result = 1
    for x in range(2, n + 1):
        value = x
        maxvalue = 0
        for xx in range(2, k + 1):
            if isprime[xx] and value % xx == 0:
                maxvalue = max(maxvalue, xx)
                while value % xx == 0:
                    value //= xx
        
        if value == 1 and maxvalue:
            result += 1

    print(result)
    
solve()