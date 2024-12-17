n, m = map(int, input().split())
j = int(input())

result = 0
left, right = 1, m
for x in range(j):
    line = int(input())
    
    if line < left:
        dist = left - line
        result += dist
        left -= dist
        right -= dist
    elif right < line:
        dist = line - right
        result += dist
        left += dist
        right += dist

print(result)