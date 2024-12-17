import sys
K = 30
MOD = 998244353
input = sys.stdin.readline 

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    brr = [[0] * 30 for _ in range(n)]
    
    comb = ((n + 1) * n) // 2
    
    for i in range(n):
        for x in range(K):
            brr[i][x] = (1 << x) & arr[i]
    
    resand = 0
    resor = 0
    resxor = 0
    
    modPOT = [(1 << x) % MOD for x in range(K)]
    
    for x in range(K):
        count = 0
        prev = 0
        for i in range(n):
            prev = (prev + 1) if brr[i][x] else 0
            count = (count + prev) % MOD
        resand = (resand + (modPOT[x] * count) % MOD) % MOD
    
    for x in range(K):
        count = 0
        prev = 0
        for i in range(n):
            prev = (prev + 1) if brr[i][x] == 0 else 0
            count = (count + prev) % MOD
        count = comb - count
        resor = (resor + (modPOT[x] * count) % MOD) % MOD
    
    for x in range(K):
        count = 0
        even = 1
        odd = 0
        for i in range(n):
            if brr[i][x]:
                odd += 1
            else:
                even += 1
            
            if brr[i][x]:
                even, odd = odd, even
            count = (count + odd) % MOD
        resxor = (resxor + (modPOT[x] * count) % MOD) % MOD
    
    print(resand, resor, resxor)

solve()