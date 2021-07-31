from queue import PriorityQueue

def bfs(board):
    
    size = len(board)
    dirr = [[0,1],[0,-1], [1,0],[-1,0]]
    
    pq = PriorityQueue()
    pq.put((0,(0,0),(0,1))) #cost, 1, 2 position
    
    board[0][0] = 1
    board[0][1] = 1
    
    while not pq.empty():
        cost, p1, p2 = pq.get()
        x1, y1 = p1
        x2, y2 = p2
        
        if (x1 == size - 1 and y1 == size - 1) or 
            (x2 == size - 1 and y2 == size -1):
                min_cost = cost
                break
        
        for xdir, ydir in dirr:
            xx1, yy1 = x1 + xdir, y1 + ydir
            xx2, yy2 = x2 + xdir, y2 + ydir
            if 0 <= xx1 < size and 0 <= yy1 < size
                and 0 <= xx2 < size and 0 <= yy2 < size
                and board[xx1][yy1] == 0 and board[xx2][yy2] == 0:
                    board[xx1][yy1] = board[xx2][yy2] = 1
                    pq.put((cost + 1, (xx1, yy1), (xx2, yy2)))
        
        if abs(x1-x2) == 1 and y1 == y2:
            if 0 <= y1 - 1 and board[x1][y1-1] == 0 and board[x2][y2-1] == 0 : #left
                board[x1][y1-1] = 1
                board[x2][y2-1] = 1
                if x1 > x2:
                    pq.put((cost + 1, (x1-1, y1-1), (x2, y2)))
                    pq.put((cost + 1, (x1, y1), (x2+1, y2-1)))
                else:
                    pq.put((cost + 1, (x1, y1), (x2-1, y2-1)))
                    pq.put((cost + 1, (x1+1, y1-1), (x2, y2)))
                
            if y1 + 1 < size and board[x1][y1+1] == 0 and board[x2][y2+1] == 0 : #right
                board[x1][y1+1] = 1
                board[x2][y2+1] = 1
                if x1 > x2:
                    pq.put((cost + 1, (x1+1, y1+1), (x2, y2)))
                    pq.put((cost + 1, (x1, y1), (x2-1, y2+1)))
                else:
                    pq.put((cost + 1, (x1, y1), (x2-1, y2+1)))
                    pq.put((cost + 1, (x1+1, y1+1), (x2, y2)))
                
        if abs(y1-y2) == 1 and x1 == x2:
            if 0 <= x1 - 1 and board[x1-1][x1] == 0 and board[x2-1][y2] == 0 : #up
                board[x1-1][y1] = 1
                board[x2-1][y2] = 1
                if y1 > y2:
                    pq.put((cost + 1, (x1-1, y1-1), (x2, y2)))
                    pq.put((cost + 1, (x1, y1), (x2+1, y2-1)))
                else:
                    pq.put((cost + 1, (x1, y1), (x2-1, y2-1)))
                    pq.put((cost + 1, (x1+1, y1-1), (x2, y2)))
                
            if x1 + 1 < size and board[x1+1][y1] == 0 and board[x2+1][y2] == 0 : #right
                board[x1][y1+1] = 1
                board[x2][y2+1] = 1
                if x1 > x2:
                    pq.put((cost + 1, (x1+1, y1+1), (x2, y2)))
                    pq.put((cost + 1, (x1, y1), (x2-1, y2+1)))
                else:
                    pq.put((cost + 1, (x1, y1), (x2-1, y2+1)))
                    pq.put((cost + 1, (x1+1, y1+1), (x2, y2)))
            

def solution(board):
    answer = bfs(board)
    return answer