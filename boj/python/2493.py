n = int(input())
top = list(map(int, input().split()))[::-1]

stack = []
answer = [0] * n

for i in range(n):
    if stack:
        while len(stack) > 0 and stack[-1][0] < top[i]:
            value, index = stack.pop()
            answer[index] = n-i
    stack.append((top[i], n-i-1))

print(*answer)