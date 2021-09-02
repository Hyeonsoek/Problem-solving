t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    rp = (r1 + r2) ** 2
    rm = (r1 - r2) ** 2

    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)
    elif d > rp:
        print(0)
    elif d == rp:
        print(1)
    elif d < rp:
        if rm < d:
            print(2)
        elif rm == d:
            print(1)
        else:
            print(0)