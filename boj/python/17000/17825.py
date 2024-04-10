board = {
    0: [i for i in range(0, 41, 2)],
    10: [i for i in range(10, 20, 3)],
    20: [i for i in range(20, 25, 2)],
    30: [i for i in range(28, 25, -1)],
    25: [i for i in range(25, 41, 5)]
}

board[30].insert(0, 30)

answer = 0

def backtracking(dice, state, idx, score):
    global answer

    # print(state, idx)

    if idx == 10:
        if answer < score:
            # print(state, score)
            answer = score
    else:
        for i, info in enumerate(state):
            vertex_idx, line = info
            # print(vertex_idx, line)
            if vertex_idx == -1: #마침
                continue

            # print(vertex_idx, line, idx)
            if vertex_idx + dice[idx] < len(board[line]):
                vertex_idx += dice[idx]
                if line == 0 and board[line][vertex_idx] in [10, 20, 30]:
                    line = board[line][vertex_idx]
                    vertex_idx = 0
            else:
                if line in [10, 20, 30]:
                    vertex_idx = vertex_idx + dice[idx] - len(board[line])
                    line = 25

                    if vertex_idx >= len(board[line]):
                        line, vertex_idx = -1, -1
                else:
                    vertex_idx, line = -1, -1

            if (vertex_idx, line) != (-1, -1):
                if [vertex_idx, line] in state:
                    continue
                if [vertex_idx, line] in [[3, 25], [20, 0]]\
                        and ([3, 25] in state or [20, 0] in state):
                    continue

            if vertex_idx >= 0:
                # print(line, vertex_idx, state, idx, dice[idx])
                score += board[line][vertex_idx]
            state[i] = [vertex_idx, line]

            backtracking(dice, state[:], idx + 1, score)

            state[i] = info
            if vertex_idx >= 0:
                score -= board[line][vertex_idx]


state = [[0, 0], [0, 0], [0, 0], [0, 0]]
dice = list(map(int, input().split()))

backtracking(dice, state[:], 0, 0)
print(answer)

# print(board[10][3])
# 3 1 1 5 4 5 3 3 2 2