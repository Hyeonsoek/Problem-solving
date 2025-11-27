def solve():
    board = [list(map(int, list(input()))) for _ in range(9)]

    empty = []
    for i in range(9):
        for j in range(9):
            if not board[i][j]:
                empty.append((i, j))
    
    def brute(empties, index):
        if index == len(empties):
            for row in board:
                print("".join(map(str, row)))
            exit()
        else:
            y, x = empties[index]
            check = [0] * 10

            for k in range(9):
                check[board[y][k]] = 1
                check[board[k][x]] = 1

            sy, sx = (y//3), (x//3)
            for yy in range(sy*3, (sy+1)*3):
                for xx in range(sx*3, (sx+1)*3):
                    check[board[yy][xx]] = 1

            for i in range(1, 10):
                if not check[i]:
                    board[y][x] = i
                    brute(empties, index+1)
                    board[y][x] = 0


    brute(empty, 0)