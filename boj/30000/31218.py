import sys
input = sys.stdin.readline

def solve():
    n, m, q = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(m + 1)]
    count = n * m
    
    result = []
    for _ in range(q):
        query = input()
        
        match query[0]:
            case '1':
                qq, dy, dx, y, x = map(int, query.split())
                while not board[y][x]:
                    board[y][x] = 1
                    count -= 1
                    
                    nx = x + dx
                    ny = y + dy
                    if ny < 1 or ny > n or nx < 1 or nx > m:
                        break
                    x, y = nx, ny
            case '2':
                qq, y, x = map(int, query.split())
                result.append(board[y][x])
            case '3':
                result.append(count)
                
    print(*result, sep='\n')
    
solve()