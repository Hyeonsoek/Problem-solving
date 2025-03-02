# import sys
# input = sys.stdin.readline

# def solve():
#     n, h_atk = map(int, input().split())
    
#     room = []
#     for _ in range(n):
#         t, a, h = map(int, input().split())
#         room.append((t, a, h))
    
#     def simulate(h_atk, h_maxhp):
#         h_curhp = h_maxhp
        
#         for t, a, h in room:
#             if t == 1:
#                 user = h / h_atk
#                 monster = h_curhp / a
# 작성중