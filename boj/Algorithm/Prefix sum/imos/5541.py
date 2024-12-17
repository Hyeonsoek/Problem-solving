from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
array = [ [0 for x in range(n + 2) ] for y in range(n + 2) ]
    
for _ in range(m):
    a, b, x = map(int, input().split())
    
    a -= 1
    b -= 1
    
    array[a][b] += 1
    array[a+x+2][b+1] += 1
    array[a+x+1][b+x+2] += 1
    
    array[a][b+1] -= 1
    array[a+x+1][b] -= 1
    array[a+x+2][b+x+2] -= 1

for x in range(n + 2):
    for y in range(1, n + 2):
        array[x][y] += array[x][y - 1]

for x in range(n + 2):
    for y in range(1, n + 2):
        array[y][x] += array[y - 1][x]

for x in range(1, n + 2):
    for y in range(x, n + 2):
        array[y][x] += array[y-1][x-1]

count = 0
for x in array:
    count += sum(map(lambda x : x > 0, x))

print(count)