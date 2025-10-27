from math import pow

def solve():
    cache = [[0] * (i + 1) for i in range(19)]
    for i in range(19):
        cache[i][0] = 1
        cache[i][-1] = 1
    
    for i in range(2, 19):
        for j in range(1, i):
            cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j]
    
    prime = [2, 3, 5, 7, 11, 13, 17]

    pa = int(input()) / 100.0
    pb = int(input()) / 100.0

    a = 0
    b = 0
    for i in prime:
        a += cache[18][i] * pow(pa, i) * pow(1 - pa, 18 - i)
        b += cache[18][i] * pow(pb, i) * pow(1 - pb, 18 - i)
    
    print(a + b - a * b)

solve()