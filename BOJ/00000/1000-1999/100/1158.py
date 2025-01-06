n, k = map(int, input().split())
queue = [*range(1, n + 1)]

index = 0
result = []
while queue:
    index = (index + k - 1) % len(queue)
    result.append(str(queue.pop(index)))

print(f'<{ ", ".join(result) }>')