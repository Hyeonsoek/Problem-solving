import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    tree = [[0, 0] for _ in range(5 * n)]

    def init(node, start, end):
        if start == end:
            tree[node][0] = 0 if arr[start] & 1 else 1
            tree[node][1] = 1 if arr[start] & 1 else 0
            return tree[node]

        mid = (start + end) // 2
        LL = init(node * 2, start, mid)
        RR = init(node * 2 + 1, mid + 1, end)

        tree[node][0] = LL[0] + RR[0]
        tree[node][1] = LL[1] + RR[1]
        return tree[node]

    def update(node, start, end, index, k):
        if start > index or end < index:
            return tree[node]

        if start == end:
            tree[node][0] = 0 if k & 1 else 1
            tree[node][1] = 1 if k & 1 else 0
            return tree[node]

        mid = (start + end) // 2
        LL = update(node * 2, start, mid, index, k)
        RR = update(node * 2 + 1, mid + 1, end, index, k)

        tree[node][0] = LL[0] + RR[0]
        tree[node][1] = LL[1] + RR[1]
        return tree[node]

    def query(node, k, start, end, left, right):
        if end < left or right < start:
            return 0

        if left <= start and end <= right:
            return tree[node][k]

        mid = (start + end) // 2
        LL = query(node * 2, k, start, mid, left, right)
        RR = query(node * 2 + 1, k, mid + 1, end, left, right)

        return LL + RR

    init(1, 0, n - 1)

    q = int(input())
    for _ in range(q):
        qq, l, r = map(int, input().split())

        if qq == 1:
            update(1, 0, n - 1, l - 1, r)
        else:
            print(query(1, qq - 2, 0, n - 1, l - 1, r - 1))


solve()