from math import ceil, log2

n = int(input())
array = [0] + sorted([ (x, index) for index, x in enumerate(map(int, input().split())) ])
tree = [0] * (1 << (ceil(log2(n)) + 1))

def _sum(node, start, end, left, right):
    if end < left or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = _sum(node * 2, start, mid, left, right)
    RR = _sum(node * 2 + 1, mid + 1, end, left, right)
    return LL + RR

def update(node, start, end, index, value):
    if index < start or end < index:
        return 0
    
    if start <= index and index <= end:
        tree[node] += value
        
    if start < end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, value)
        update(node * 2 + 1, mid + 1, end, index, value)
        
result = 0

for x in range(1, n + 1):
    result += _sum(1, 1, n, array[x][1], n)
    update(1, 1, n, array[x][1], 1)
        
print(result)