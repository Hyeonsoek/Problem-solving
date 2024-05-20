# import sys
# from bisect import *
# from collections import defaultdict
# input = sys.stdin.readline

# def quadrant(x, y):
#     if x > 0 and y > 0:
#         return 1
#     elif x < 0 and y > 0:
#         return 2
#     elif x < 0 and y < 0:
#         return 3
#     else:
#         return 4

# n, m = map(int, input().split())

# linear = defaultdict(list)
# for _ in range(n):
#     fx, fy = map(int, input().split())
    
#     if fy == 0:
#         key = '-x' if fx < 0 else 'x'
#         linear[key].append(fx)
#     elif fx == 0:
#         key = '-y' if fy < 0 else 'y'
#         linear[key].append(fy)
#     else:
#         key = (quadrant(fx, fy), fy / fx)
#         linear[key].append(fx)
        
# for key in linear:
#     linear[key].sort()

# result = 0
# for _ in range(m):
#     ex, ey = map(int, input().split())
#     if ey == 0:
#         xkey = '-x' if ex < 0 else 'x'
#         target = bisect_right(linear[xkey], ex)
#     elif ex == 0:
#         ykey = '-y' if ey < 0 else 'y'
#         target = bisect_right(linear[ykey], ey)
#     else:
#         key = (quadrant(ex, ey), ey / ex)
#         target = bisect_right(linear[key], ex)
        
#     result = max(result, target)
    
# print(result)

# 작성중 틀린 코드