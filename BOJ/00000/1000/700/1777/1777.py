import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    tree = [0] * 4 * n
    
    def init(node=1, start=1, end=n):
        if start == end:
            tree[node] = 1
            return tree[node]
        
        mid = (start + end) >> 1
        LL = init(node << 1, start, mid)
        RR = init(node << 1 | 1, mid + 1, end)
        tree[node] = LL + RR
        return tree[node]

    def update(index, node=1, start=1, end=n):
        if index < start or end < index:
            return tree[node]
        
        if start == end:
            tree[node] -= 1
            return tree[node]
        
        mid = (start + end) >> 1
        LL = update(index, node << 1, start, mid)
        RR = update(index, node << 1 | 1, mid + 1, end)
        tree[node] = LL + RR
        return tree[node]
    
    def query(value, node=1, start=1, end=n):
        if start == end:
            return start
        
        mid = (start + end) >> 1
        if tree[node << 1 | 1] >= value:
            return query(value, node << 1 | 1, mid + 1, end)
        return query(value - tree[node << 1 | 1], node << 1, start, mid)
    
    init()
    
    result = [0] * n
    for x in reversed(range(1, n + 1)):
        index = query(arr[x - 1] + 1)
        update(index)
        result[index - 1] = x
    
    print(*result)
    
solve()