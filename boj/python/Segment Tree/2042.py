import sys, math
input = sys.stdin.readline

n, m, k = map(int, input().split())
array = [ int(input()) for _ in range(n) ]

height = int(math.log2(n)) + 2
tree = [ 0 ] * (1 << height)

def init(node, start, end):
    if start == end:
        tree[node] = array[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        left = init(node * 2, start, mid)
        right = init(node * 2 + 1, mid + 1, end)
        tree[node] = left + right
        return tree[node]

def sum(node, start, end, left, right):
    if left > end or start > right:
        return 0
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return sum(node * 2, start, mid, left, right) + sum(node * 2 + 1, mid + 1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or end < index:
        return
    
    tree[node] += diff
    
    if start < end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)
        

init(1, 0, n - 1)

for x in range(m + k):
    a, b, c = map(int, input().split())
    
    if a == 1:
        update(1, 0, n - 1, b - 1, c - array[b - 1])
        array[b - 1] = c
    else:
        print(sum(1, 0, n - 1, b - 1, c - 1))