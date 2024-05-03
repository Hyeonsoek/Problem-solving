import sys, math
input = sys.stdin.readline

MOD = 1000000007

n, m, k = map(int, input().split())
array = [0] + [int(input()) for _ in range(n)]

height = 1 << (int(math.ceil(math.log2(n))) + 1)
tree = [1] * height

def init(node, start, end):
    if start == end:
        tree[node] = array[start]
        return tree[node]

    mid = (start + end) // 2
    LL = init(node * 2, start, mid)
    RR = init(node * 2 + 1, mid + 1, end)
    tree[node] = ((LL % MOD) * (RR % MOD)) % MOD
    return tree[node]

def multi(node, start, end, left, right):
    if left > end or start > right:
        return 1
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = multi(node * 2, start, mid, left, right)
    RR = multi(node * 2 + 1, mid + 1, end, left, right)
    
    return (LL * RR) % MOD

def update(node, start, end, index, newValue):
    if index < start or end < index:
        return tree[node]
    
    if start == end:
        tree[node] = newValue
        return tree[node]
    
    if start < end:
        mid = (start + end) // 2
        RR = update(node * 2, start, mid, index, newValue)
        LL = update(node * 2 + 1, mid + 1, end, index, newValue)
        tree[node] = ((RR % MOD) * (LL % MOD)) % MOD
        return tree[node]
 
init(1, 1, n)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    
    if a == 1:
        update(1, 1, n, b, c)
    else:
        print(multi(1, 1, n, b, c))