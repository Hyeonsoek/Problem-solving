ddir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n = int(input())
array = [ list(map(str, input().split())) for _ in range(n) ]

teacher = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 'T':
            teacher.append((i, j))

def check() -> bool:
    for x, y in teacher:
        for xd, yd in ddir:
            xx, yy = x + xd, y + yd
            while 0 <= xx < n and 0 <= yy < n and array[xx][yy] != 'O':
                if array[xx][yy] == 'S':
                    return False
                xx += xd
                yy += yd
    return True

def brute(x : int, y : int, count : int) -> bool:
    if count == 0:
        return check()
    elif x == 0 and y == n and count > 0:
        return False
    else:
        result = False
        
        nx = 0 if x + 1 == n else x + 1
        ny = y + 1 if x + 1 == n else y
        
        if array[x][y] == 'X':
            array[x][y] = 'O'
            result |= brute(nx, ny, count-1)
            array[x][y] = 'X'
            
        result |= brute(nx, ny, count)
        
        return result


print("YES" if brute(0, 0, 3) else "NO")