def simulate(x, d, k):
    global n, m, circle

    for mx in range(x-1, n, x):
        if d == 0:
            for _ in range(k):
                value = circle[mx].pop()
                circle[mx].insert(0, value)
        else:
            for _ in range(k):
                circle[mx].append(circle[mx][0])
                del circle[mx][0]

    count = 0
    check = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if circle[i][j] == 0:
                continue
            count += 1

            if circle[i][j] == circle[i][cw[j]]:
                check[i][j] = 1
                check[i][cw[j]] = 1

            if circle[i][j] == circle[i][ccw[j]]:
                check[i][j] = 1
                check[i][ccw[j]] = 1

            if i > 0 and circle[i][j] == circle[i-1][j]:
                check[i][j] = 1
                check[i-1][j] = 1

            if i < n-1 and circle[i][j] == circle[i+1][j]:
                check[i][j] = 1
                check[i+1][j] = 1

    if sum(map(sum, check)) == 0 and count > 0:
        value = sum(map(sum, circle)) / count
        for i in range(n):
            for j in range(m):
                if circle[i][j] == 0:
                    continue
                if circle[i][j] > value:
                    circle[i][j] -= 1
                elif circle[i][j] < value:
                    circle[i][j] += 1
    else:
        for i in range(n):
            for j in range(m):
                if check[i][j]:
                    circle[i][j] = 0


n, m, t = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(n)]

cw = {i: i+1 for i in range(m)}
ccw = {i: i-1 for i in range(m)}

cw[m-1] = 0
ccw[0] = m - 1

for _ in range(t):
    xx, dd, kk = map(int, input().split())
    simulate(xx, dd, kk)

answer = sum(map(sum, circle))
print(answer)

# 4 6 1
# 1 2 3 4 5 6
# 2 3 4 5 6 7
# 3 4 5 6 7 8
# 4 5 6 7 8 9
# 2 1 2