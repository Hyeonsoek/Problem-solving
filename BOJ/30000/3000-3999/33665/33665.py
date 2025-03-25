def solve():
    weight = [[*map(int, input().split())] for _ in range(10)]
    
    def to_list(tstr):
        tstr = [*map(int, tstr)]
        board = [[0] * 4 for _ in range(10)]
        for i in range(10):
            for j in range(4):
                board[i][j] = tstr[i * 4 + j]
        return board
    
    own = to_list(input())
    trade = to_list(input())
    pawn = to_list(input())

    cashA = int(input())
    cashB = int(input())
    
    showA = int(input())
    showB = int(input())
    
    rate = int(input())
    penalty = int(input())
    
    def get_weight(cashA, cashB):
        w = [0, int(cashA * rate / 100), int(cashB * rate / 100)]
        counter = [[0] * 3 for _ in range(10)]
        for i in range(10):
            for j in range(4):
                counter[i][own[i][j]] += 1
                if pawn[i][j]:
                    w[own[i][j]] -= penalty
        
        for i in range(10):
            for j in range(1, 3):
                if counter[i][j]:
                    w[j] += weight[i][counter[i][j] - 1]
                    
        return w[1], w[2]
    
    oA, oB = get_weight(cashA, cashB)
    
    cashA += showB - showA
    cashB += showA - showB
    
    for i in range(10):
        for j in range(4):
            if trade[i][j]:
                own[i][j] = trade[i][j]
                
    tA, tB = get_weight(cashA, cashB)
    
    if (oA - oB) <= (tA - tB):
        return "YES"
    return "NO"

print(solve())