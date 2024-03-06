import sys


def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())

    width = 1 << 16
    tree = [0 for _ in range(4 * width)]

    def update(node, start, end, index, diff):
        if index < start or end < index:
            return tree[node]

        if start == end:
            tree[node] += diff
            return tree[node]

        mid = (start + end) // 2
        ll = update(node * 2, start, mid, index, diff)
        rr = update(node * 2 + 1, mid + 1, end, index, diff)
        tree[node] = ll + rr

        return tree[node]

    def query(node, start, end, kth):
        if start == end:
            return start

        mid = (start + end) // 2
        ll = tree[node * 2]

        if ll >= kth:
            return query(node * 2, start, mid, kth)
        else:
            return query(node * 2 + 1, mid + 1, end, kth - ll)

    arr = [int(input()) for _ in range(n)]

    for x in range(k-1):
        update(1, 0, width, arr[x], 1)

    result = 0
    target = (k // 2) + (1 if k & 1 else 0)
    for x in range(k-1, n):
        update(1, 0, width, arr[x], 1)
        result += query(1, 0, width, target)
        update(1, 0, width, arr[x - k + 1], -1)

    return result


print(solve())