MOD = 1000000009
MAX = 100001

def solve():
    cache = [[0, 0] for _ in range(MAX)]
    cache[0][0] = 0
    cache[0][1] = 1
    
    for x in range(1, MAX):
        for y in range(1, 4):
            if x >= y:
                odd = cache[x - y][0]
                even = cache[x - y][1]
                
                cache[x][0] = (cache[x][0] + even) % MOD
                cache[x][1] = (cache[x][1] + odd) % MOD
    
    n = int(input())
    for x in range(n):
        print(*cache[int(input())])
        
solve()