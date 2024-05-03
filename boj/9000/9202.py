from sys import stdin
from collections import defaultdict

dir_ = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def bruteforce(count, score, string, y, x, board, check):
    global MAX_string

    # print(string)

    if dict_[string]:
        dict_[string] = False
        count += 1
        score += score_[len(string)]
        if len(MAX_string) < len(string):
            MAX_string = string[:]
        elif len(MAX_string) == len(string):
            MAX_string = min(MAX_string, string)

    if len(string) == 8:
        return count, score
    else:
        new_count, new_score = 0, 0

        for yd, xd in dir_:
            yy = yd + y
            xx = xd + x
            if 0 <= yy < 4 and 0 <= xx < 4 and check[yy][xx]:
                check[yy][xx] = 0
                cc, ss = bruteforce(0, 0, string + board[yy][xx], yy, xx, board, check)
                new_count += cc
                new_score += ss
                check[yy][xx] = 1

        return count + new_count, score + new_score


n = int(input())
dict_ = defaultdict(bool)
score_ = defaultdict(int)

score_[3] = score_[4] = 1
score_[5] = 2
score_[6] = 3
score_[7] = 5
score_[8] = 11

string_list = [stdin.readline().strip() for _ in range(n)]

input()

k = int(input())

for bn in range(k):
    MAX_count = 0
    MAX_string = ''
    MAX_score = 0
    check_board = [[1] * 4 for _ in range(4)]

    for index in string_list:
        dict_[index] = True

    BOARD = [list(input()) for _ in range(4)]

    for i in range(4):
        for j in range(4):
            check_board[i][j] = 0
            ci, si = bruteforce(0, 0, BOARD[i][j], i, j, BOARD, check_board)
            MAX_count += ci
            MAX_score += si
            check_board[i][j] = 1

    print(MAX_score, MAX_string, MAX_count)

    if bn < k-1:
        input()