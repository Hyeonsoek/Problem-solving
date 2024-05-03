import sys
sys.setrecursionlimit(1000000)
MAX = sys.maxsize
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tree = [[0, -1] for _ in range(4 * n)]


def init(node, start, end):
    if start == end:
        tree[node][0] = arr[start]
        tree[node][1] = start
        return tree[node]

    mid = (start + end) // 2
    ll = init(node * 2, start, mid)
    rr = init(node * 2 + 1, mid + 1, end)

    tree[node][0] = ll[0] + rr[0]

    if ll[1] == -1:
        tree[node][1] = rr[1]

    if rr[1] == -1:
        tree[node][1] = ll[1]

    if rr[1] != -1 and ll[1] != -1:
        tree[node][1] = ll[1] if arr[ll[1]] < arr[rr[1]] else rr[1]

    return tree[node]


def query(left, right, node=1, start=0, end=n-1):
    if left > end or start > right:
        return [0, -1]

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    ll = query(left, right, node * 2, start, mid)
    rr = query(left, right, node * 2 + 1, mid + 1, end)

    _sum = ll[0] + rr[0]

    if ll[1] == -1:
        return [_sum, rr[1]]
    elif rr[1] == -1:
        return [_sum, ll[1]]

    return [_sum, ll[1] if arr[ll[1]] < arr[rr[1]] else rr[1]]


def dnq(left, right):
    _sum, _min_index = query(left, right)

    if _min_index == -1:
        return 0

    points = _sum * arr[_min_index]

    if left < _min_index:
        points = max(points, dnq(left, _min_index - 1))

    if _min_index < right:
        points = max(points, dnq(_min_index + 1, right))

    return points


init(1, 0, n - 1)
print(dnq(0, n - 1))