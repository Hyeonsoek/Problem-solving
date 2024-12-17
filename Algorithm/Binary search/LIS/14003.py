import bisect

n = int(input())
array = list(map(int, input().split()))

indexes = [-1 for x in range(n)]

lis = [array[0]]
indexes[0] = 0

for x in range(1, n):
    target = array[x]
    if lis[-1] < target:
        lis.append(target)
        indexes[x] = len(lis) - 1
    else:
        index = bisect.bisect_left(lis, target)
        lis[index] = target
        indexes[x] = index
        
print(len(lis))

count = len(lis) - 1
answer = []
for x in range(n - 1, -1, -1):
    if indexes[x] == count:
        answer.append(array[x])
        count -= 1

print(*answer[::-1])