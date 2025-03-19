# import sys
# input = sys.stdin.readline

# def solve():
#     n, m, q = map(int, input().split())
    
#     forw = [0] * (n + 2)
#     back = [0] * (n + 2)
#     for _ in range(m):
#         w, d = map(int, input().split())
#         forw[w] += d
#         back[w] += d

#     for i in range(1, n + 2):
#         forw[i] += forw[i - 1]
    
#     for i in reversed(range(n + 1)):
#         back[i] += back[i + 1]
    
#     s = 0
#     e = n + 1
#     for _ in range(q):
#         p = int(input())
        
#         if s < p < e:
#             f = forw[p] - forw[s]
#             b = back[p] - back[e]

#             if f > b:
#                 e = p
#                 print(b)
#             elif f < b:
#                 s = p
#                 print(f)
#             else:
#                 if p > n - p:
#                     e = p
#                     print(b)
#                 else:
#                     s = p
#                     print(f)
#         else:
#             print(0)

# solve()