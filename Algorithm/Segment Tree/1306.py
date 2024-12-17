from math import ceil, log2

MIN = -1

n, m = map(int, input().split())
array = [0] + list(map(int, input().split()))
tree = [0] * (1 << (ceil(log2(n) + 1)) + 1)

def init(node, start, end):
    if start == end:
        tree[node] = array[start]
    else:
        mid = (start + end) // 2
        LL = init(node * 2, start, mid)
        RR = init(node * 2 + 1, mid + 1, end)
        tree[node] = max(LL, RR)
        
    return tree[node]

def _max(node, start, end, left, right):
    if end < left or right < start:
        return MIN
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = _max(node * 2, start, mid, left, right)
    RR = _max(node * 2 + 1, mid + 1, end, left, right)
    
    return max(LL, RR)

init(1, 1, n)

results = [ _max(1, 1, n, x - m + 1, x + m - 1) for x in range(m, n - m + 2) ]
print(*results)