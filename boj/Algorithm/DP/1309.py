n = int(input())
cache = [3, 7, *[0] * (n)]

for x in range(2, n):
    cache[x] = (2 * cache[x-1] + cache[x - 2]) % 9901

print(cache[n-1])

# import sys
# MOD = 9901
# sys.setrecursionlimit(200000)

# n = int(input())
# cache = [[-1] * 3 for _ in range(n + 1)]

# def dp(x, index):
#     if x == 0:
#         return 1
    
#     if cache[x][index] != -1:
#         return cache[x][index]
    
#     cache[x][index] = dp(x - 1, 0) % MOD
#     if index != 1:
#         cache[x][index] += dp(x - 1, 2)
#         cache[x][index] %= MOD
    
#     if index != 2:
#         cache[x][index] += dp(x - 1, 1)
#         cache[x][index] %= MOD
        
#     return cache[x][index]

# print(dp(n, 0))