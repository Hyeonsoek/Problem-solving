n = int(input())
for _ in range(n):
    a, b = map(lambda x: int(x, 2), input().split())
    print(bin(a + b)[2:])