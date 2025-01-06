dirr = [[0, 1], [-1, 0], [0, -1], [1, 0]]
board = [[0] * 101 for _ in range(101)]
curve = {0: 1, 1: 2, 2: 3, 3: 0}

def generate_dragon_curve(d, g):
    result = [d]
    for _ in range(g):
        reverse = result[::-1]
        for dd in reverse:
            result.append(curve[dd])
    return result

n = int(input())
for _ in range(n):
    x, y, d, g = map(int, input().split())
    result = generate_dragon_curve(d, g)

    yy, xx = y, x
    for dd in result:
        board[yy][xx] = 1
        yy, xx = yy + dirr[dd][0], xx + dirr[dd][1]
    board[yy][xx] = 1

answer = 0
for y in range(100):
    for x in range(100):
        if board[y][x] == board[y][x+1] ==\
                board[y+1][x] == board[y+1][x+1] == 1:
            answer += 1
print(answer)

