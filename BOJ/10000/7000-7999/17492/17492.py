drx = [-1, -1, -1, 0, 0, 1, 1, 1]
dry = [-1, 0, 1, -1, 1, -1, 0, 1]

def solve():
    n = int(input())
    board = [[*map(int, input().split())] for _ in range(n)]
    
    stones = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 2:
                stones.append((x, y))
    
    def brute(stone : list[tuple], count):
        if count == 1:
            return True
        else:
            result = False
            nstones = stone[:]
            for x in range(len(stone)):
                xx, yy = stone[x]
                for d in range(8):
                    lx = xx + drx[d]
                    ly = yy + dry[d]
                    nx = xx + drx[d] * 2
                    ny = yy + dry[d] * 2
                    
                    if lx < 0 or n <= lx or ly < 0 or n <= ly:
                        continue
                    
                    if nx < 0 or n <= nx or ny < 0 or n <= ny:
                        continue
                    
                    if board[lx][ly] != 2 or board[nx][ny] != 0:
                        continue
                    
                    nstones.remove((lx, ly))
                    nstones.remove((xx, yy))
                    nstones.append((nx, ny))
                    
                    board[lx][ly] = board[xx][yy] = 0
                    board[nx][ny] = 2
                    result |= brute(nstones[:], count - 1)
                    board[nx][ny] = 0
                    board[lx][ly] = board[xx][yy]  = 2
                    
                    nstones.remove((nx, ny))
                    nstones.append((lx, ly))
                    nstones.append((xx, yy))
            
            return result
    
    print('Possible' if brute(stones, len(stones)) else 'Impossible')

solve()