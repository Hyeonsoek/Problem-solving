dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def seat_batch(num, likes):
    can_sit = []

    for y in range(n):
        for x in range(n):
            if board[y][x] > 0:
                continue

            empty = 0
            like_count = 0
            for ydir, xdir in dirr:
                yy = y + ydir
                xx = x + xdir

                if 0 <= yy < n and 0 <= xx < n:
                    if board[yy][xx] in likes:
                        like_count += 1
                    if board[yy][xx] == 0:
                        empty += 1

            can_sit.append([like_count, empty, y, x])

    can_sit.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    _, _, y, x = can_sit[0]
    board[y][x] = num

def result():
    answer = 0
    for y in range(n):
        for x in range(n):
            like_count = 0
            for ydir, xdir in dirr:
                yy = y + ydir
                xx = x + xdir

                if 0 <= yy < n and 0 <= xx < n:
                    if board[yy][xx] in likes_info[board[y][x]]:
                        like_count += 1

            answer += 0 if not like_count else 10**(like_count-1)

    return answer


n = int(input())
board = [[0] * n for _ in range(n)]
likes_info = {}

for _ in range(n*n):
    line = list(map(int, input().split()))
    nn, ll = line[0], line[1:]
    likes_info[nn] = ll
    seat_batch(nn, ll)

print(result())