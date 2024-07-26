# import sys
# dirr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# input = sys.stdin.readline

# def solve():
#     h, w = map(int, input().split())
#     r, c, d = map(int, input().split())
#     rule = [
#         [list(map(int, input().strip())) for _ in range(h)], # A
#         [list(map(int, input().strip())) for _ in range(h)]  # B
#     ]
    
#     board = [[1] * w for _ in range(h)]
#     parent = [x for x in range(h * w * 4 * 2)]
    
#     def to_vertex(rr, cc, dd, tt):
#         return tt * 4 * w * h + dd * w * h + rr * w + cc
    
#     def find(u):
#         if parent[u] == u:
#             return u
#         parent[u] = find(parent[u])
#         return parent[u]
    
#     def merge(u, v):
#         u = find(u)
#         v = find(v)
        
#         if u == v:
#             return False
    
#         parent[u] = v
        
#         return True
    
#     print(len(rule), len(rule[0]), len(rule[0][0]))
    
#     t = 0
#     result = 0
#     while True:
#         current = to_vertex(r, c, d, t)

#         dd = (d + rule[t][r][c]) % 4
#         rr = r + dirr[dd][0]
#         cc = c + dirr[dd][1]
        
#         if not (0 <= rr < h and 0 <= cc < w):
#             break
        
#         tt = 1 - board[rr][cc]
#         next = to_vertex(rr, cc, dd, tt)
        
#         print(current, next)
        
#         if not merge(current, next):
#             print("MERGE")
#             break
        
#         print('---------------')
#         print('\t', t, d, r, c)
        
#         result += 1
#         board[r][c] = 0
#         r, c, d, t = rr, cc, dd, tt
    
#         print('\t', tt, dd, rr, cc)
#         for x in range(h):
#             print(*board[x])
#         print('---------------')
    
#     print(result)

# solve()