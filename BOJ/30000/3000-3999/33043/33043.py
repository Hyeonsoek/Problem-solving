# from collections import *

# INDEX = {}

# for k, j in enumerate(['m', 'p', 's']):
#     for i in range(1, 10):
#         INDEX[str(i) + j] = k * 9 + (i - 1)

# INDEX.update({str(x) + 'z' : 26 + x for x in range(1, 8)})

# def sub(a, b):
#     return [a[i] - b[i] for i in range(34)]

# def solve():
#     n = int(input())
#     arr = input().split()
    
#     prefix = [[0] * 34]
    
#     for i in range(1, n + 1):
#         prefix.append(prefix[-1][:])
#         prefix[-1][INDEX[arr[i - 1]]] += 1
    
    
#     def isValid(mid):
#         for i in range(mid, n + 1):
#             subprefix = sub(prefix[i], prefix[i - mid])
#             print(i, subprefix)
#             if any(j > 4 for j in subprefix):
#                 return False
#         return True
    
#     low, high = 1, n
#     while low < high:
#         mid = (low + high) // 2
#         print(low, high, mid)
        
#         if isValid(mid):
#             high = mid - 1
#         else:
#             low = mid + 1
    
#     return low

# print(solve())