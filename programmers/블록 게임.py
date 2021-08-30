def is_delete_block(board, y, x):
    value = board[y][x]
    
    case = [
                [ [value, 0, 0], [value, value, value], [0, 0, 0] ],
                [ [0, value, 0], [0, value, 0], [value, value, 0] ],
                [ [0, 0, value], [value, value, value], [0, 0, 0] ],
                [ [0, value, 0], [0, value, 0], [0, value, value] ],
                [ [0, value, 0], [value, value, value], [0, 0, 0] ]
            ]

    upward = [
                [ (y-1, x), (y-1, x+1) ],
                [ (y, x-1) ],
                [ (y-1, x), (y-1, x-1) ],
                [ (y, x+1) ],
                [ (y-1, x-1), (y-1, x+1)]
            ]

    for i in range(5):
        count = 0
        for yy in range(y-1, y+2):
            for xx in range(x-1, x+2):
                if 0 <= yy < len(board) and 0 <= xx < len(board) \
                        and board[yy][xx] > 0 and board[yy][xx] == case[i][yy-y+1][xx-x+1]:
                    count += 1

        if count == 4:
            for ny, nx in upward[i]:
                if 0 <= ny < len(board) and 0 <= nx < len(board):
                    for yy in range(ny, -1, -1):
                        if board[yy][nx] > 0 and board[yy][nx] != value:
                            return False
            return True
    
    return False

    
def delete_block(board, y, x):
    value = board[y][x]
    
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == value:
                board[y][x] = 0
    
def search_block(board):
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] > 0 and is_delete_block(board, y, x):
                delete_block(board, y, x)
                return 1
    return 0
    
def solution(board):

    answer = 0

    while True:
        result = search_block(board)
        if result == 1:
            answer += result
        else:
            break
    
    return answer

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))
print(solution([[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]]))
print(solution([[0, 2, 0, 0], [1, 2, 2, 4], [1, 2, 0, 4], [1, 1, 4, 4]]))
print(solution([[0, 1, 0, 2], [1, 1, 1, 2], [0, 3, 2, 2], [0, 3, 3, 3]]))
print(solution([[1, 0, 0, 2], [1, 1, 0, 2], [1, 3, 2, 2], [0, 3, 3, 3]]))