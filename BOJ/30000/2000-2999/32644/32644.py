import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = [0, *map(int, input().split())]
    tree = [0] * (n + 1)

    def update(x, value):
        while x <= n:
            tree[x] += value
            x += x & -x

    def query(x):
        result = 0
        while x > 0:
            result += tree[x]
            x -= x & -x
        return result

    for x in range(1, n + 1):
        update(x, arr[x])

    result = []
    for x in map(int, input().split()):
        e = query(x)
        result.append(e)
        update(x, -arr[x])

    print(*result)

solve()

# 1 3 6 10 15
# 