from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    q = deque([(l[i], i) for i in range(n)])

    answer = 0
    while q:
        value, idx = q.popleft()

        if [(v, i) for v, i in q if value < v]:
            q.append((value, idx))
        else:
            answer += 1
            if idx == m:
                break

    print(answer)
