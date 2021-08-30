## 다시푸는중~

from queue import PriorityQueue

def is_in_board(size, x, y):
    return 0 <= x < size and 0 <= y < size

def bfs(board):

    min_cost = 0
    size = len(board)

    check = [[0] * size for _ in range(size)]
    dirr = [[0,1],[0,-1], [1,0],[-1,0]]
    
    pq = PriorityQueue()
    pq.put((0,(0,0),(0,1))) #cost, 1, 2 position
    
    while not pq.empty():
        cost, p1, p2 = pq.get()
        x1, y1 = p1
        x2, y2 = p2
        
        if (x1 == size - 1 and y1 == size - 1) or \
            (x2 == size - 1 and y2 == size -1):
                min_cost = cost
                break
        
        for xdir, ydir in dirr:
            xx1, yy1 = x1 + xdir, y1 + ydir
            xx2, yy2 = x2 + xdir, y2 + ydir
            if is_in_board(size, xx1, yy1) \
                and is_in_board(size, xx2, yy2) \
                and board[xx1][yy1] == 0 and board[xx2][yy2] == 0:
                    board[xx1][yy1] = board[xx2][yy2] = 1
                    pq.put((cost + 1, (xx1, yy1), (xx2, yy2)))
        


    return min_cost

def solution(board):
    answer = bfs(board)
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))