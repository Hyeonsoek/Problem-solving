import sys, bisect
input = sys.stdin.readline

n = int(input())
array = sorted([ list(map(int, input().split())) for _ in range(n) ])
indexes = [ -1 for _ in range(n) ]

lis = [ array[0][1] ]
indexes[0] = 0

for x in range(1, n):
    target = array[x][1]
    if lis[-1] < target:
        lis.append(target)
        indexes[x] = len(lis) - 1
    else:
        index = bisect.bisect_left(lis, target)
        lis[index] = target
        indexes[x] = index

answer = []
index = len(lis) - 1

for x in range(n - 1, -1, -1):
    if indexes[x] == index:
        index -= 1
    else:
        answer.append(array[x][0])

print(len(answer))
for x in answer[::-1]:
    print(x)