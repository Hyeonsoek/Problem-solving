def solve():
    xx, yy = map(int, input().split())
    m = xx * yy
    print(2, m - xx, yy - m)

solve()