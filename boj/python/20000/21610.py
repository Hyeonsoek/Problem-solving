import copy

def water_copy_bug():
    dirr = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    for y, x in prev_cloud:
        count = 0
        for ydir, xdir in dirr:
            yy = y + ydir
            xx = x + xdir
            if 0 <= yy < n and 0 <= xx < n and board[yy][xx] > 0:
                count += 1
        board[y][x] += count

def make_cloud():
    global board, cloud, prev_cloud
    for y in range(n):
        for x in range(n):
            if board[y][x] >= 2 and (y, x) not in prev_cloud:
                board[y][x] -= 2
                cloud.append((y, x))

def move_cloud(d, s):
    global cloud

    dirr = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    for idx in range(len(cloud)):
        y, x = cloud[idx]
        yy = (y + dirr[d-1][0] * s) % n
        xx = (x + dirr[d-1][1] * s) % n
        cloud[idx] = (yy, xx)
        board[yy][xx] += 1

def remove_cloud():
    global prev_cloud
    prev_cloud = copy.deepcopy(cloud)
    cloud.clear()

def rain_thirster():
    for d, s in move_info:
        move_cloud(d, s)
        remove_cloud()
        water_copy_bug()
        make_cloud()

    return sum(map(sum, board))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move_info = [tuple(map(int, input().split())) for _ in range(m)]
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
prev_cloud = []

print(rain_thirster())