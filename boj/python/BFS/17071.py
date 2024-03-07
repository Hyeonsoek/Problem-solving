from collections import deque
MAX = 500001


def sovle():
    n, k = map(int, input().split())

    visited = [[-1] * 2 for _ in range(MAX)]
    visited[n][0] = 0

    queue = deque([(0, n)])

    while queue:
        second, x = queue.popleft()
        index = (second + 1) % 2

        for xx in [x-1, x+1, x*2]:
            if 0 <= xx < MAX and visited[xx][index] == -1:
                visited[xx][index] = second + 1
                queue.append((second + 1, xx))

    dest = k
    for time in range(MAX):
        dest += time
        if dest >= MAX:
            break
        if 0 <= visited[dest][time % 2] <= time:
            return time

    return -1


print(sovle())