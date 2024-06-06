n, a, b = map(int, input().split())

result = 0
while a != b:
    a = (a + (1 if a & 1 else 0)) // 2
    b = (b + (1 if b & 1 else 0)) // 2
    result += 1

print(result)