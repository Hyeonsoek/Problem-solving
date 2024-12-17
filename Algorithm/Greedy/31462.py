import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [list(input().strip()) for _ in range(n)]
    visited = [[False] * len(arr[x]) for x in range(n)]

    for y in range(n-1):
        for x in range(len(arr[y])):
            if not visited[y][x] and not visited[y+1][x] and not visited[y+1][x+1]\
                    and arr[y][x] == 'R' and arr[y + 1][x] == 'R' and arr[y + 1][x + 1] == 'R':
                visited[y][x] = True
                visited[y+1][x] = True
                visited[y+1][x+1] = True

    for y in range(n-1, 1, -1):
        for x in range(1, len(arr[y]) - 1):
            if not visited[y][x] and not visited[y - 1][x - 1] and not visited[y - 1][x] \
                    and arr[y][x] == 'B' and arr[y - 1][x - 1] == 'B' and arr[y - 1][x] == 'B':
                visited[y][x] = True
                visited[y-1][x] = True
                visited[y-1][x-1] = True

    result = True
    for y in visited:
        for x in y:
            result &= x

    print(1 if result else 0)

solve()