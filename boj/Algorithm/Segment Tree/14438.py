import sys, math
input = sys.stdin.readline
MAX = 10 ** 9

def init(node, start, end):
    if start == end:
        tree[node] = array[start]
        return tree[node]

    mid = (start + end) // 2
    LL = init(node * 2, start, mid)
    RR = init(node * 2 + 1, mid + 1, end)
    tree[node] = min(LL, RR)
    return tree[node]

def update(node, start, end, index, value):
    if index < start or end < index:
        return
    
    if start == end:
        tree[node] += value
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, index, value)
    update(node * 2 + 1, mid + 1, end, index, value)
    
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def query(node, start, end, left, right) -> int:
    if right < start or end < left:
        return MAX
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = query(node * 2, start, mid, left, right)
    RR = query(node * 2 + 1, mid + 1, end, left, right)
    return min(LL, RR)

n = int(input())
array = [ 0 ] + list(map(int, input().split()))

width = 1 << (math.ceil(math.log2(n)) + 1) + 1
tree = [ 0 ] * width

init(1, 1, n)

m = int(input())
for _ in range(m):
    q, a, b = map(int, input().split())
    
    if q == 1:
        update(1, 1, n, a, b - array[a])
        array[a] = b
    elif q == 2:
        print(query(1, 1, n, a, b))