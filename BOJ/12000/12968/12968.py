def solve():
    r, c, k = map(int, input().split())
    if k == 1:
        return 1
    return 1 - (r * c) & 1

print(solve())