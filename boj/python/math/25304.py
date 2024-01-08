x = int(input())
n = int(input())
s = sum(map(lambda x : x[0] * x[1], [ list(map(int, input().split())) for _ in range(n) ]))
print("Yes" if s == x else "No")