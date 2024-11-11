import sys
input = sys.stdin.readline

def dynamic(graph, n, m, char):
    cost = [[0] * m for _ in range(n)]
    costR = [[0] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            c = int(graph[x][y] == char)
            cost[x][y] += c
            costR[x][y] += c
    
    for x in range(1, m):
        cost[0][x] += cost[0][x-1]
        costR[n-1][m-x-1] += costR[n-1][m-x]
    
    for x in range(1, n):
        cost[x][0] += cost[x-1][0]
        costR[n-x-1][m-1] += costR[n-x][m-1]
    
    for x in range(1, n):
        for y in range(1, m):
            cost[x][y] += max(cost[x-1][y], cost[x][y-1])
            costR[n-x-1][m-y-1] += max(costR[n-x][m-y-1], costR[n-x-1][m-y])
    
    costL = [[0] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if x != 0 and y != 0 and y + 1 < m and x + 1 < n:
                costL[x][y] = cost[x][y] + max(costR[0][y+1], costR[x+1][0])
            elif x != 0 and y + 1 < m:
                costL[x][y] = cost[x][y] + costR[0][y+1]
            elif y != 0 and x + 1 < n:
                costL[x][y] = cost[x][y] + costR[x+1][0]
            else:
                costL[x][y] = costR[x][y]

    return max(map(max, costL))

def solve():
    n, m = map(int, input().split())
    board = [input().split() for _ in range(n)]
    
    result = []
    for char in 'ZOAC':
        result.append(dynamic(board, n, m, char))
    
    print(*result)

solve()