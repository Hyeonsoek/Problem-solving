from sys import stdin

ccw = {0: 3, 1: 0, 2: 1, 3: 2}
dirr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
sand_ratio = [0.01, 0.01, 0.02, 0.07, 0.07, 0.02, 0.1, 0.1, 0.05]

def spread_sand(y, x, d):
    global n, board
    remainder = board[y + dirr[d][0]][x + dirr[d][1]]
    outer_board = 0
    ratio_idx = 0

    if d in [0, 2]:
        check = [[x-1, x+1], [x-2, x-1, x+1, x+2], [x-1, x+1], [x]]
        for s in range(4):
            for xx in check[s]:
                yy = y + dirr[d][0] * s
                value = int(sand_ratio[ratio_idx] * board[y + dirr[d][0]][x + dirr[d][1]])
                remainder -= value
                if 0 <= yy < n and 0 <= xx < n:
                    board[yy][xx] += value
                else:
                    outer_board += value
                ratio_idx += 1

        yy = y + dirr[d][0] * 2
        if 0 <= yy < n and 0 <= x < n:
            board[yy][x] += remainder
        else:
            outer_board += remainder

        board[y + dirr[d][0]][x] = 0
    else:
        check = [[y-1, y+1], [y-2, y-1, y+1, y+2], [y-1, y+1], [y]]
        for s in range(4):
            for yy in check[s]:
                xx = x + dirr[d][1] * s
                value = int(sand_ratio[ratio_idx] * board[y + dirr[d][0]][x + dirr[d][1]])
                remainder -= value
                if 0 <= yy < n and 0 <= xx < n:
                    board[yy][xx] += value
                else:
                    outer_board += value
                ratio_idx += 1

        xx = x + dirr[d][1] * 2
        if 0 <= y < n and 0 <= xx < n:
            board[y][xx] += remainder
        else:
            outer_board += remainder

        board[y][x + dirr[d][1]] = 0

    return y + dirr[d][0], x + dirr[d][1], outer_board

def tornado():
    global n, board

    answer = 0

    y, x, d = (n-1)//2, (n-1)//2, 3
    for square in range(1, n):
        for _ in range(2):
            for _ in range(square):
                y, x, outer_board = spread_sand(y, x, d)
                answer += outer_board
            d = ccw[d]

    for _ in range(n-1):
        y, x, outer_board = spread_sand(y, x, d)
        answer += outer_board

    return answer


n = int(input())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

print(tornado())