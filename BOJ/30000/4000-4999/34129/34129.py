# import sys
# input = sys.stdin.readline

# def solve():
#     n, k = map(int, input().split())
#     arr = sorted([*map(int, input().split())])
    
#     svalue = 0
#     ans = []
#     for i in range(n - 1):
#         if svalue + arr[i] < k:
#             svalue += arr[i]
#             ans.append((i, arr[i]))
#         else:
#             for k, (j, v) in enumerate(reversed(ans)):
#                 nextv = svalue - v + arr[i]
#                 if svalue < nextv < k:
#                     svalue = nextv
                    