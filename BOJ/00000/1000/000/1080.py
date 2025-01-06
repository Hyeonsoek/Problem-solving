def solve():
    n, m = map(int, input().split())
    maxtrixA = [list(map(lambda x: bool(int(x)), list(input()))) for _ in range(n)]
    maxtrixB = [list(map(lambda x: bool(int(x)), list(input()))) for _ in range(n)]
    
    def flip(x, y):
        for dx in range(3):
            for dy in range(3):
                maxtrixA[x + dx][y + dy] ^= True
    
    count = 0
    for x in range(n-2):
        for y in range(m-2):
            if maxtrixA[x][y] != maxtrixB[x][y]:
                flip(x, y)
                count += 1
    
    for x in range(n):
        for y in range(m):
            if maxtrixA[x][y] != maxtrixB[x][y]:
                return -1
            
    return count

print(solve())