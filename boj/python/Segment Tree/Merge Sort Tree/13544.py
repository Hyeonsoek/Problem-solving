import bisect
import sys
input = sys.stdin.readline

def merge(tree, node):
    left = tree[node << 1]
    right = tree[node << 1 | 1]
    p, q = 0, 0
    while p < len(left) and q < len(right):
        if left[p] < right[q]:
            tree[node].append(left[p])
            p += 1
        else:
            tree[node].append(right[q])
            q += 1

    if q == len(right):
        for x in range(p, len(left)):
            tree[node].append(left[x])
    else:
        for x in range(q, len(right)):
            tree[node].append(right[x])

def build(tree, arr, node, start, end):
    if start == end:
        tree[node].append(arr[start])
        return

    mid = (start + end) // 2
    build(tree, arr, node << 1, start, mid)
    build(tree, arr, node << 1 | 1, mid + 1, end)

    merge(tree, node)

def query(tree, node, start, end, left, right, k):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return len(tree[node]) - bisect.bisect_right(tree[node], k)

    mid = (start + end) // 2
    LL = query(tree, node << 1, start, mid, left, right, k)
    RR = query(tree, node << 1 | 1, mid + 1, end, left, right, k)
    return LL + RR

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [[] for _ in range(4*n)]
    build(tree, arr, 1, 0, n - 1)

    result = 0
    qn = int(input())
    for _ in range(qn):
        left, right, k = map(lambda x: int(x) ^ result, input().split())
        result = query(tree, 1, 0, n - 1, left - 1, right - 1, k)
        print(result)

solve()