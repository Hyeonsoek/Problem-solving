import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [0, *map(int, input().split())]
    tree = [0] * 4 * n
    
    def init(node=1, start=1, end=n):
        if start == end:
            tree[node] = arr[start]
            return tree[node]

        mid = (start + end) >> 1
        LL = init(node << 1, start, mid)
        RR = init(node << 1 | 1, mid + 1, end)
        tree[node] = LL + RR
        return tree[node]

    def update(index, value, node=1, start=1, end=n):
        if index < start or end < index:
            return tree[node]
        
        if start == end:
            tree[node] += value
            return tree[node]
        
        mid = (start + end) >> 1
        LL = update(index, value, node << 1, start, mid)
        RR = update(index, value, node << 1 | 1, mid + 1, end)
        tree[node] = LL + RR
        
        return tree[node]

    def query(value, node=1, start=1, end=n):
        if start == end:
            return start
        
        mid = (start + end) >> 1
        if tree[node << 1] >= value:
            return query(value, node << 1, start, mid)
        return query(value - tree[node << 1], node << 1 | 1, mid + 1, end)
    
    init()
    
    m = int(input())
    for _ in range(m):
        q, *a = map(int, input().split())
        
        if q & 1:
            index, value = a
            update(index, value)
        else:
            value = a[0]
            print(query(value))
            
solve()