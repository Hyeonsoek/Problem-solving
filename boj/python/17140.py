from collections import Counter

def counterSort(array):
    counter = Counter(array).most_common()
    return sorted(counter, key=lambda x: (x[1], x[0]))

def inner_op(board, target):
    for y in board:
        counter = counterSort(y)
        row = []
        for x in counter:
            if x[0] > 0:
                row.append(x[0])
                row.append(x[1])
        target.append(row)

    max_row = len(max(target, key=len))
    for y in target:
        for _ in range(max_row - len(y)):
            y.append(0)

def operation(board):
    R, C = len(board), len(board[0])
    newboard = []

    if R >= C:
        inner_op(board, newboard)
    else:
        rboard = list(map(list, zip(*board)))
        inner_op(rboard, newboard)
        newboard = list(map(list, zip(*newboard)))

    # print("--------------------")
    # for y in newboard:
    #     print(*y)

    return newboard


r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

for i in range(101):
    if len(board) >= r and len(board[0]) >= c and board[r-1][c-1] == k:
        print(i)
        exit()
    board = operation(board)

print(-1)