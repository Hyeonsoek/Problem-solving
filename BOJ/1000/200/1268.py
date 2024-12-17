import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

index = 0
max_value = 0
for x in range(n):
    count = set()
    for y in range(n):
        for z in range(5):
            if arr[x][z] == arr[y][z]:
                count.add(y)

    if max_value < len(count):
        index = x
        max_value = len(count)

print(index + 1)