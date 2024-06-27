from collections import deque

def solve():
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    if n == 1:
        return 1

    result = deque([arr.pop(), arr.pop()])
    for x in range(2, n):
        value = arr.pop()
        if result[-1] > value:
            result.append(value)
        elif result[0] > value:
            result.appendleft(value)

    return len(result)

print(solve())