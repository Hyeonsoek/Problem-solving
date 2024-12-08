def solve():
    D, K = map(int, input().split())
    
    cache = [[0, 0] for _ in range(D)]
    cache[0] = [1, 0]
    cache[1] = [0, 1]
    
    for i in range(2, D):
        cache[i][0] = cache[i-2][0] + cache[i-1][0]
        cache[i][1] = cache[i-2][1] + cache[i-1][1]
    
    aa, bb = cache[D-1]
    for A in range(1, K + 1):
        R = K - A * aa
        if R % bb == 0:
            B = R // bb
            print(A)
            print(B)
            return

solve()