def is_unlock(x,y,N,board):
    for xx in range(x,x+N):
        for yy in range(y,y+N):
            if board[xx][yy] != 1:
                return False
    return True

def rotate_key(key):
    return list(zip(*key[::-1]))
    
def put_key(x, y, key, board):
    for xx in range(x, x+len(key)):
        for yy in range(y, y+len(key)):
            board[xx][yy] += key[xx-x][yy-y]
    
    return board

def remove_key(x,y,key, board):
    for xx in range(x, x+len(key)):
        for yy in range(y, y+len(key)):
            board[xx][yy] -= key[xx-x][yy-y]
        
    return board

# 몰라서 다른사람 코드 보고했다... 더 정진해야지...
def solution(key, lock):
    N = len(lock)
    M = len(key)
    board = [ [ 0 ] * (2*M + N) for x in range(2 * M + N) ]
    put_key(M,M,lock,board)
    
    for _ in range(4):
        key = rotate_key(key)
        for x in range(M + N):
            for y in range(M + N):
                put_key(x,y,key, board)
                if is_unlock(M,M,N,board):
                    return True
                remove_key(x,y,key,board)
    
    return False