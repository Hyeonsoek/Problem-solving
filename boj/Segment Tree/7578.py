import sys, math
input = sys.stdin.readline

def update(node, start, end, index, value):
    if index < start or end < index:
        return
    
    if start == end:
        tree[node] += value
        return
    
    mid = (start + end) >> 1
    update(node << 1, start, mid, index, value)
    update((node << 1) + 1, mid + 1, end, index, value)
    
    tree[node] = tree[node << 1] + tree[(node << 1) + 1]

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) >> 1
    LL = query(node << 1, start, mid, left, right)
    RR = query((node << 1) + 1, mid + 1, end, left, right)
    return LL + RR

n = int(input())
upper = list(map(int, input().split()))
under = list(map(int, input().split()))

width = 1 << (math.ceil(math.log2(n)) + 1)
tree = [0] * width

dic = {}
for idx, num in enumerate(under):
    dic[num] = idx + 1
    
result = 0
for x in range(n):
    q = query(1, 1, n, dic[upper[x]] + 1, n)
    result += q
    update(1, 1, n, dic[upper[x]], 1)

print(result)