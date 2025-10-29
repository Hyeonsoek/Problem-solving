import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 0, -1, 1]

def solve():
    n = int(input())
    arr = [[*map(int, input().split())] for _ in range(n + 1)]
    cache = [[sys.maxsize] * 5 for _ in range(n + 1)]
    for i in range(5):
        cache[0][i] = 1
    cache[0][2] = 0

    for i in range(1, n + 1):
        for s in range(5):
            sx = arr[i - 1][0] + dx[s]
            sy = arr[i - 1][1] + dy[s]
            for e in range(5):
                ex = arr[i][0] + dx[e]
                ey = arr[i][1] + dy[e]
                cache[i][e] = min(cache[i][e], cache[i-1][s] + abs(sx-ex) + abs(sy-ey))

    print(min(cache[n]))

solve()


# import sys
# sys.setrecursionlimit(10000000)
# input = sys.stdin.readline

# dx = [-1, 1, 0, 0, 0]
# dy = [0, 0, 0, -1, 1]

# def solve():
#     n = int(input())
#     arr = [[*map(int, input().split())] for _ in range(n + 1)]
#     cache = [[-1] * 5 for _ in range(n + 1)]
#     def dynamic(index, loc):
#         if cache[index][loc] != -1:
#             return cache[index][loc]
        
#         sx = arr[index][0] + dx[loc]
#         sy = arr[index][1] + dy[loc]
#         res = sys.maxsize
#         if index + 1 <= n:
#             for k in range(5):
#                 ex = arr[index + 1][0] + dx[k]
#                 ey = arr[index + 1][1] + dy[k]
#                 res = min(res, dynamic(index + 1, k) + abs(ex - sx) + abs(ey - sy))
#         else:
#             res = 0
        
#         cache[index][loc] = res
#         return res
    
#     r = sys.maxsize
#     for i in range(5):
#         r = min(r, dynamic(0, i) + (i != 2))
#     print(r)

# solve()