import sys
input = sys.stdin.readline

# def solve():
#     n = int(input())
#     point = sorted([tuple(map(int, input().split())) for _ in range(n)])
#     point = [ (point[x][1], point[x][0]) for x in range(n) ]
    
#     stack = [point[0]]
#     for index in range(1, n):
#         maxTuple = (0, 0)
#         for x in range(index, n):
#             maxTuple = max(maxTuple, point[x])
#             if stack[-1] < point[x]:
#                 stack.append(point[x])
#                 break
#         else:
#             if stack[-1] != maxTuple:
#                 stack.append(maxTuple)
    
#     result = 0
#     for x in range(1, len(stack)):
#         y1, x1 = stack[x-1]
#         y2, x2 = stack[x]
#         if y1 < y2:
#             result += (x2 - x1) * y1
#         else:
#             result += y1 + (x2 - x1 - 1) * y2
            
#     result += stack[-1][0]
    
#     print(result)

def solve():
    n = int(input())
    board = [0] * 1001
    for _ in range(n):
        l, h = map(int, input().split())
        board[l] = h

    result = 0
    left = 0
    for x in range(1, 1001):
        if board[x] > board[left]:
            result += board[left] * (x - left)
            left = x
    
    right = 0
    for x in reversed(range(left, 1001)):
        if board[x] > board[right]:
            result += board[right] * (right - x)
            right = x
        
    result += board[left] * (right - left + 1)
    print(result)

solve()