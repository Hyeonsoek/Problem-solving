n, k = map(int, input().split())
arr = list(input())

result = 0
visited = [False] * n
for x in range(n):
    if arr[x] == 'H':
        for y in range(x-k, x+k+1):
            if 0 <= y < n and not visited[y] and arr[y] == 'P':
                visited[y] = True
                result += 1
                break

print(result)