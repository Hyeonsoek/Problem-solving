import sys

MAX = 1000000001
input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    tree = [[0, 0] for _ in range(5 * n)]

    def init(node, start, end):
        if start == end:
            tree[node][0] = arr[start]
            tree[node][1] = start
            return tree[node]

        mid = (start + end) // 2
        LL = init(node * 2, start, mid)
        RR = init(node * 2 + 1, mid + 1, end)

        if LL[0] <= RR[0]:
            tree[node][0] = LL[0]
            tree[node][1] = LL[1]
        else:
            tree[node][0] = RR[0]
            tree[node][1] = RR[1]

        return tree[node]

    def update(node, start, end, index, k):
        if start > index or end < index:
            return tree[node]

        if start == end:
            tree[node][0] = k
            return tree[node]

        mid = (start + end) // 2
        LL = update(node * 2, start, mid, index, k)
        RR = update(node * 2 + 1, mid + 1, end, index, k)

        if LL[0] <= RR[0]:
            tree[node][0] = LL[0]
            tree[node][1] = LL[1]
        else:
            tree[node][0] = RR[0]
            tree[node][1] = RR[1]

        return tree[node]

    def query(node, start, end, left, right):
        if end < left or right < start:
            return [MAX, 0]

        if left <= start and end <= right:
            return tree[node]

        mid = (start + end) // 2
        LL = query(node * 2, start, mid, left, right)
        RR = query(node * 2 + 1, mid + 1, end, left, right)

        if LL[0] <= RR[0]:
            return LL
        else:
            return RR

    init(1, 0, n - 1)

    q = int(input())
    for _ in range(q):
        qq, l, r = map(int, input().split())

        if qq == 1:
            update(1, 0, n - 1, l - 1, r)
        else:
            print(query(1, 0, n - 1, l - 1, r - 1)[1] + 1)


solve()