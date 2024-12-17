dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def solve():
    board = [list(input().split()) for _ in range(5)]
    
    s = set()
    
    def backtrack(x, y, curr, count):
        if count == 0:
            s.add(int(curr))
        else:
            for xdir, ydir in dirr:
                xx = x + xdir
                yy = y + ydir
                if 0 <= xx < 5 and 0 <= yy < 5:
                    backtrack(xx, yy, curr + board[xx][yy], count - 1)
    
    for x in range(5):
        for y in range(5):
            backtrack(x, y, board[x][y], 5)
        
    print(len(s))

solve()