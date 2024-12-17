import sys
from math import log2, ceil
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    tree = [0] * (n + 1)

    height = ceil(log2(n)) + 1
    tree = [ -1 for _ in range(1 + (1 << height)) ]
    
    def init(node, start, end):
        if start == end:
            tree[node] = arr[start]
            return
        
        mid = (start + end) // 2
        init(node * 2, start, mid)
        init(node * 2 + 1, mid + 1, end)
        
        LL = tree[node * 2]
        RR = tree[node * 2 + 1]
        
        tree[node] = max(LL, RR)

    def query(node, start, end, left, right):
        if right < start or end < left:
            return -1
        
        if left <= start and end <= right:
            return tree[node]
        
        mid = (start + end) // 2
        LL = query(node * 2, start, mid, left, right)
        RR = query(node * 2 + 1, mid + 1, end, left, right)
        
        return max(LL, RR)

    init(1, 0, n - 1)
    
    indexes = [-1] * (n + 1)
    for x in range(n):
        if indexes[arr[x]] != -1:
            section_max = query(1, 0, n - 1, indexes[arr[x]] + 1, x - 1)
            if arr[x] < section_max:
                return False
            
        indexes[arr[x]] = x
    
    return True

t = int(input())
for _ in range(t):
    result = solve()
    print("Yes" if result else "No")