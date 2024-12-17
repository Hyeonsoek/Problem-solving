def solve():
    n, m = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(n)]
    
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
        
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            prefix[x][y] += prefix[x][y -1] + board[x-1][y-1]

    for y in range(1, m + 1):
        for x in range(1, n + 1):
            prefix[x][y] += prefix[x-1][y]

    def range_sum(sx, sy, ex, ey):
        return prefix[ex][ey] - prefix[sx-1][ey] - prefix[ex][sy-1] + prefix[sx-1][sy-1]
    
    def mult_sliced_sum(points):
        value = 1
        for sx, sy, ex, ey in points:
            value *= range_sum(sx, sy, ex, ey)
        return value
    
    result = 0
    for width1 in range(1, m - 1):
        for width2 in range(1, m - width1):
            result = max(result, mult_sliced_sum([
                (1, 1, n, width1),
                (1, width1 + 1, n, width1 + width2),
                (1, width1 + width2 + 1, n, m)
            ]))
            
    for height1 in range(1, n - 1):
        for height2 in range(1, n - height1):
            result = max(result, mult_sliced_sum([
                (1, 1, height1, m),
                (height1 + 1, 1, height1 + height2, m),
                (height1 + height2 + 1, 1, n, m)
            ]))
    
    for height in range(1, n):
        for width in range(1, m):
            result = max(result, mult_sliced_sum([
                (1, 1, height, width),
                (1, width + 1, height, m),
                (height + 1, 1, n, m)
            ]))
            
            result = max(result, mult_sliced_sum([
                (1, 1, height, width),
                (1, width + 1, n, m),
                (height + 1, 1, n, width)
            ]))
            
            result = max(result, mult_sliced_sum([
                (1, 1, n, m - width),
                (1, m - width + 1, height, m),
                (height + 1, m - width + 1, n, m)
            ]))
            
            result = max(result, mult_sliced_sum([
                (1, 1, n - height, m),
                (n - height + 1, 1, n, width),
                (n - height + 1, width + 1, n, m)
            ]))
    
    print(result)

solve()


# class Prefix:
#     def __init__(self, n, m, board) -> None:
#         self.prefix = [[0] * (m + 1) for _ in range(n + 1)]
        
#         for x in range(1, n + 1):
#             for y in range(1, m + 1):
#                 self.prefix[x][y] += self.prefix[x][y -1] + board[x-1][y-1]
    
#         for y in range(1, m + 1):
#             for x in range(1, n + 1):
#                 self.prefix[x][y] += self.prefix[x-1][y]
                
#     def range_sum(self, sx, sy, ex, ey):
#         return self.prefix[ex][ey] - self.prefix[sx-1][ey] - self.prefix[ex][sy-1] + self.prefix[sx-1][sy-1]
    
#     def mult_sliced_sum(self, points):
#         value = 1
#         for sx, sy, ex, ey in points:
#             value *= self.range_sum(sx, sy, ex, ey)
#         return value

# def solve():
#     n, m = map(int, input().split())
#     board = [list(map(int, list(input()))) for _ in range(n)]
#     prefix = Prefix(n, m, board)
    
#     result = 0
#     # 3-slice width
#     for width1 in range(1, m - 1):
#         for width2 in range(1, m - width1):
#             result = max(result, prefix.mult_sliced_sum([
#                 (1, 1, n, width1),
#                 (1, width1 + 1, n, width1 + width2),
#                 (1, width1 + width2 + 1, n, m)
#             ]))
            
#     # 3-slice height
#     for height1 in range(1, n - 1):
#         for height2 in range(1, n - height1):
#             result = max(result, prefix.mult_sliced_sum([
#                 (1, 1, height1, m),
#                 (height1 + 1, 1, height1 + height2, m),
#                 (height1 + height2 + 1, 1, n, m)
#             ]))
    
#     # 3-slice height and width
#     for height in range(1, n):
#         for width in range(1, m):
#             # height slice at 1, 1
#             result = max(result, prefix.mult_sliced_sum([
#                 (1, 1, height, width),
#                 (1, width + 1, height, m),
#                 (height + 1, 1, n, m)
#             ]))
            
#             # width slice at 1, 1
#             result = max(result, prefix.mult_sliced_sum([
#                 (1, 1, height, width),
#                 (1, width + 1, n, m),
#                 (height + 1, 1, n, width)
#             ]))
            
#             # width slice at 1, m
#             result = max(result, prefix.mult_sliced_sum([
#                 (1, 1, n, m - width),
#                 (1, m - width + 1, height, m),
#                 (height + 1, m - width + 1, n, m)
#             ]))
            
#             # heigt slice at n, 1
#             result = max(result, prefix.mult_sliced_sum([
#                 (1, 1, n - height, m),
#                 (n - height + 1, 1, n, width),
#                 (n - height + 1, width + 1, n, m)
#             ]))
    
#     print(result)

# solve()