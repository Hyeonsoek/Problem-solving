import sys
sys.setrecursionlimit(300000)

def solve():
    board = [[*map(int, input().split())] for _ in range(3)]
    
    def who(o):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == o:
                return True
            if board[0][i] == board[1][i] == board[2][i] == o:
                return True
        
        if board[0][0] == board[1][1] == board[2][2] == o:
            return True
        
        if board[0][2] == board[1][1] == board[2][0] == o:
            return True
        
        return False
    
    def backtrack(o, cnt):
        if who(1):
            return 1
        if who(2):
            return 2
        
        if cnt == 0:
            return 0
        
        op = 2 if o == 1 else 1
        ret = op
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = o
                    v = backtrack(op, cnt - 1)
                    board[i][j] = 0
                    
                    if o == v:
                        return o
                    ret = min(ret, v)
        
        return ret
    
    counts = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            counts[board[i][j]] += 1
    
    start = 1 if counts[1] == counts[2] else 2
    v = backtrack(start, counts[0])
    if v == 0:
        print("D")
    else:
        print("W" if v == start else "L")

solve()