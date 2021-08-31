from collections import deque
from collections import defaultdict

def is_in_board(size, x, y):
    return 0 <= x < size and 0 <= y < size

def loc_string(p):
    return '.'.join(list(map(str, p)))

def bfs(board):

    min_cost = 0
    size = len(board)

    dirr = [[0,1],[0,-1], [1,0],[-1,0]]

    check = defaultdict(int)
    pq = deque()
    pq.append((0,[0,0,0,1])) #cost, 1, 2 position
    check[loc_string([0, 0, 0, 1])] = 1

    while pq:
        cost, p = pq.popleft()
        x1, y1, x2, y2 = p

        if (x1 == size - 1 and y1 == size - 1) or \
            (x2 == size - 1 and y2 == size -1):
                return cost

        for xdir, ydir in dirr:
            xx1, yy1 = x1 + xdir, y1 + ydir
            xx2, yy2 = x2 + xdir, y2 + ydir
            if is_in_board(size, xx1, yy1) \
                    and is_in_board(size, xx2, yy2) \
                    and board[xx1][yy1] == 0 and board[xx2][yy2] == 0:

                string = loc_string([xx1, yy1, xx2, yy2])
                if check[string] == 0:
                    check[string] = 1
                    pq.append((cost + 1, [xx1, yy1, xx2, yy2]))

                string = loc_string([x1, y1, xx1, yy1])
                if check[string] == 0:
                    check[string] = 1
                    pq.append((cost + 1, [x1, y1, xx1, yy1]))

                string = loc_string([xx2, yy2, x2, y2])
                if check[string] == 0:
                    check[string] = 1
                    pq.append((cost + 1, [xx2, yy2, x2, y2]))

    return -1

def solution(board):
    answer = bfs(board)
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))