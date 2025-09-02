MOD = 10 ** 9

def solve():
    n = int(input())
    cache = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(n + 1)]
    
    for i in range(1, 10):
        cache[1][i][1 << i] = 1
    
    for i in range(2, n + 1):
        for k in range(1 << 10):
            cache[i][0][k | 1] += cache[i - 1][1][k]
            
        for k in range(1 << 10):
            cache[i][9][k | (1 << 9)] += cache[i - 1][8][k]
        
        for j in range(1, 9):
            for k in range(1 << 10):
                l = k | (1 << j)
                cache[i][j][l] += (cache[i - 1][j + 1][k] + cache[i - 1][j - 1][k]) % MOD
                cache[i][j][l] %= MOD
    
    answer = 0
    for i in range(10):
        answer += cache[n][i][1023]
        answer %= MOD
    
    print(answer)
    
solve()