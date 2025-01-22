# import sys
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     arr = sorted([*map(int, input().split())])
    
#     cache = [[0] * 40001 for _ in range(n + 1)]
#     cache[0][0] = 1
    
#     for i in range(1, n + 1):
#         for j in range(arr[i - 1], 40001):
#             if cache[i - 1][j - arr[i - 1]] == 1:
#                 cache[i][j] = 1
    
    
    
#     k = int(input())
#     query = [*map(int, input().split())]
    
#     for i in range(n + 1):
#         print(*cache[i][:40])
    
#     result = []
#     for i in query:
#         for j in range(1, n + 1):
#             if cache[j][i]:
#                 result.append('Y')
#                 break
#         else:
#             result.append('N')
    
#     print(*result)
    
# solve()