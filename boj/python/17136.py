MAX = 987654321
answer = MAX

def check(board):
    return not sum(map(sum, board))

def check_put(board, y, x, length):
    for i in range(y, y+length):
        for j in range(x, x+length):
            if board[i][j] == 0:
                return False
    return True

def put_paper(board, y, x, length, value):
    for i in range(y, y + length):
        for j in range(x, x + length):
            board[i][j] = value

def bruteforce(count, confetti, board, y, x):
    global answer

    # print(y, x)

    if check(board):
        if answer > count:
            answer = count
    elif (y, x) == (10, 0):
        return
    else:
        ny = y + 1 if x == 9 else y
        nx = 0 if x == 9 else x + 1

        if board[y][x] == 1:
            for length in range(5, 0, -1):
                if y + length <= 10 \
                        and x + length <= 10 \
                        and check_put(board, y, x, length) \
                        and confetti[length-1] > 0:
                    put_paper(board, y, x, length, 0)
                    confetti[length-1] -= 1
                    bruteforce(count + 1, confetti[:], board, ny, nx)
                    confetti[length-1] += 1
                    put_paper(board, y, x, length, 1)
        else:
            bruteforce(count, confetti[:], board, ny, nx)


BOARD = [list(map(int, input().split())) for _ in range(10)]
CONFETTI = [5] * 5

bruteforce(0, CONFETTI, BOARD, 0, 0)
print(-1 if answer == MAX else answer)