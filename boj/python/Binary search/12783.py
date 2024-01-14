import bisect

n = int(input())
array = list(map(int, input().split()))

answer = [array[0]]

for x in array[1:]:
    if answer[-1] < x:
        answer.append(x)
    else:
        index = bisect.bisect_left(answer, x)
        answer[index] = x

print(len(answer))