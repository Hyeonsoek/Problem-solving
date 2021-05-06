from queue import PriorityQueue


#BFS든 DFS든 조건만 잘 세웠으면 쉽게 풀리는...
def solution(board):
    
    n = len(board)
    check = [ [987654321 for x in range(n)] \
                    for y in range(n) ]
    direction = [[0,1],[0,-1],[-1,0],[1,0]]
    pq = PriorityQueue()
    pq.put((0,0,0,0))
    pq.put((0,0,0,1))
    
    check[0][0] = 0
    
    while not pq.empty():
        location = pq.get()
        
        x = location[0]
        y = location[1]
        cost = location[2]
        line = location[3]
        
        for d in direction:
            xx = x + d[0]
            yy = y + d[1]
            if xx >= 0 and xx < n and yy >= 0 and yy < n \
                and board[xx][yy] == 0:
                
                if yy == y:
                    add_cost = 100 if line == 1 else 600
                    trans_line = 1
                if xx == x:
                    add_cost = 100 if line == 0 else 600
                    trans_line = 0

                if add_cost + cost <= check[xx][yy]:
                    check[xx][yy] = add_cost + cost
                    pq.put((xx,yy,cost + add_cost,trans_line))
                
    return check[n-1][n-1]