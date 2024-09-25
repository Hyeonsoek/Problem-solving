inputmap = lambda: map(int, input().split())

def solve():
    n1, m1 = inputmap()
    board1 = [[0] * 150 for _ in range(150)]
    for x in range(n1):
        line = [*map(int, input())]
        for y in range(m1):
            board1[x+50][y+50] = line[y]
    
    n2, m2 = inputmap()
    board2 = [[*map(int, input())] for _ in range(n2)]
    
    def concat(x, y):
        result = 2500
        for xx in range(x, x + n2):
            for yy in range(y, y + m2):
                if board1[xx][yy] and board2[xx-x][yy-y]:
                    return result
        
        minx = min(x, 50)
        maxx = max(x + n2, n1 + 50)
        miny = min(y, 50)
        maxy = max(y + m2, m1 + 50)
        
        result = (maxx - minx) * (maxy - miny)        
        return result
    
    result = 2500
    for x in range(4):
        for x in range(150 - n2):
            for y in range(150 - m2):
                result = min(result, concat(x, y))
        board2 = list(map(list, zip(*board2[::-1])))
        n2, m2 = m2, n2
        
    print(result)

solve()