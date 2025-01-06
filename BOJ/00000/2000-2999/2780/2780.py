MOD = 1234567

def solve():
    graph = [
        [7],
        [2,4],
        [1,3,5],
        [2,6],
        [1,5,7],
        [2,4,6,8],
        [3,5,9],
        [4,8,0],
        [5,7,9],
        [6,8]
    ]

    cache = [[0] * 10 for _ in range(1002)]
    for x in range(10):
        cache[0][x] = 1
    
    for x in range(1, 1001):
        for xx in range(10):
            for k in graph[xx]:
                cache[x][xx] += cache[x-1][k]
    
    t = int(input())
    for _ in range(t):
        print(sum(cache[int(input())-1]) % MOD)

solve()