n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n) ]
b = [list(map(int, input().split())) for _ in range(n) ]

for x in range(n):
    c = [ a[x][y] + b[x][y] for y in range(m) ]
    print(" ".join(map(str, c)))