def check_4_block(y, x, board):
    value = board[y][x]

    if value == '0':
        return False

    for yy in [y, y+1]:
        for xx in [x, x+1]:
            if board[yy][xx] != value: 
                return False

    return True

def change_4_block(y, x, board):
    cnt = 0

    for yy in [y, y+1]:
        for xx in [x, x+1]:
            if board[yy][xx] != '0':
                board[yy][xx] = '0'
                cnt+=1

    return board, cnt

def line_zero_up(n, m, board):
    for y in range(n):
        if '0' in board[y]:
            while '0' in board[y]:
                board[y].remove('0')

            while len(board[y]) < m:
                board[y].insert(0, '0')

    return board

def solution(m, n, board):
    answer = 0

    board = list(zip(*board))

    for x in range(n):
        board[x] = list(board[x])

    while True:
        block_loc = []
        for x in range(m-1):
            for y in range(n-1):
                if check_4_block(y, x, board):
                    block_loc.append([y, x])

        if not block_loc:
            break

        for y, x in block_loc:
            board, cnt = change_4_block(y, x, board)
            answer += cnt

        board = line_zero_up(n, m, board)

    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))