import sys
from bisect import *
input = sys.stdin.readline

def solve():
    n = int(input())
    tree = [[0, n + 1] for _ in range(4 * n)]
    height = {}
    
    def query(left, right, node = 1, start = 1, end = n):
        if end < left or right < start:
            return 0, n + 1
        
        if left <= start and end <= right:
            return tree[node]
        
        mid = (start + end) >> 1
        LL = query(left, right, node << 1, start, mid)
        RR = query(left, right, (node << 1) + 1, mid + 1, end)
        
        maxvalue = max(LL[0], RR[0])
        minvalue = min(LL[1], RR[1])
        
        return maxvalue, minvalue
    
    def update(index, node = 1, start = 1, end = n):
        if index < start or end < index:
            return tree[node]
        
        if start == end:
            tree[node][0] = tree[node][1] = index
            return tree[node]

        mid = (start + end) >> 1
        LL = update(index, node << 1, start, mid)
        RR = update(index, (node << 1) + 1, mid + 1, end)
        tree[node][0] = max(LL[0], RR[0])
        tree[node][1] = min(LL[1], RR[1])

        return tree[node]
    
    r = 0
    result = [0]
    root = int(input())
    height[root] = 0
    height[0] = 0
    height[n + 1] = 0
    update(root)
    for _ in range(1, n):
        k = int(input())
        left = query(1, k - 1)[0]
        right = query(k + 1, n)[1]
        height[k] = max(height[left], height[right]) + 1
        r += height[k]
        update(k)
        result.append(r)

    print(*result, sep='\n')

solve()