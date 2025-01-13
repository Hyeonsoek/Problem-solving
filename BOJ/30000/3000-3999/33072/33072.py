# import sys
# from bisect import *
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     C = [*map(int, input().split())]
#     P = [*map(int, input().split())]
#     a, b = map(int, input().split())
    
#     K = sum(P)
#     V = sum(C)
#     cache = {K : V}
#     for i in range(n):
#         T = {}
#         for j, v in cache.items():
#             X = j - P[i]
#             if X >= 0:
#                 if X in cache:
#                     T[X] = min(cache[X], v - C[i])
#                 else:
#                     T[X] = v - C[i]
#         cache.update(T)

#     cacheV = {}
#     for k, v in cache.items():
#         d = a * v - b * k
#         if d in cacheV:
#             cacheV[d] = min(cacheV[d], k)
#         else:
#             cacheV[d] = k

#     cacheValue, cacheResult = zip(*sorted(cacheV.items()))
    
#     m = len(cacheValue)
#     q = int(input())
#     for _ in range(q):
#         c, p = map(int, input().split())
        
#         d = b * p - a * c
        
#         if d >= 0:
#             print(0)
#         else:
#             i = bisect_right(cacheValue, d)
            
#             if i == 0:
#                 print(-1)
#             elif i == m:
#                 print(0)
#             else:
#                 print(cacheResult[i - 1])

# solve()