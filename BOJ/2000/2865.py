n, m, k = map(int, input().split())
scores = [0] * n
for _ in range(m):
    arr = list(map(float, input().split()))
    for x in range(n):
        num, score = int(arr[2*x]) - 1, arr[2*x+1]
        scores[num] = max(scores[num], score)

answer = sum(sorted(scores, reverse=True)[:k])
print(round(answer, 1))