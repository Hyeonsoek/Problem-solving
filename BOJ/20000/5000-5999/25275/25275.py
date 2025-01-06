def solve():
    n = int(input())
    board = [[*map(int, input())] for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(n):
            count += board[i][j]
    
    def isLine(row=True):
        for i in range(n):
            tempCnt = count
            for j in range(n):
                if row:
                    tempCnt += -1 if board[i][j] else 1
                else:
                    tempCnt += -1 if board[j][i] else 1
            if tempCnt <= n:
                return True
        return False

    isRow = isLine()
    isColumn = isLine(False)
    
    if isRow and isColumn:
        return '+'
    
    if isRow:
        return '-'
    return '|'

print(solve())