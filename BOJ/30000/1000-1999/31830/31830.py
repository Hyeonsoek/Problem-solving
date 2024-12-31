import sys
input = sys.stdin.readline
print = sys.stdout.write
        
def solve():
    n, m = map(int, input().split())
    arr = list(map(lambda x: ord(x)-ord('A')+1, input().strip()))
    D = [arr[0]] + [arr[x] - arr[x-1] for x in range(1, n)] + [0]
    E = [1 if D[x] else 0 for x in range(n)] + [0]
    tree = [0 for _ in range(4*n)]
        
    def init(node=1, start=0, end=n):
        if start == end:
            tree[node] = E[start]
            return
        
        node2 = node << 1
        mid = (start + end) >> 1
        init(node2, start, mid)
        init(1 + node2, mid + 1, end)
        
        tree[node] = tree[node2] + tree[1 + node2]
        
    def query(left, right, node=1, start=0, end=n):
        if right < start or end < left:
            return 0
        
        if left <= start and end <= right:
            return tree[node]
        
        node2 = node << 1
        mid = (start + end) >> 1
        LL = query(left, right, node2, start, mid)
        RR = query(left, right, 1 + node2, mid + 1, end)
        return LL + RR
            
    def update(index, value, node=1, start=0, end=n):
        if index < start or end < index:
            return
        
        if start == end:
            D[start] += value
            D[start] = 0 if D[start] in [26, -26] else D[start]
            tree[node] = 1 if D[start] else 0
            return
        
        node2 = node << 1
        mid = (start + end) >> 1
        update(index, value, node2, start, mid)
        update(index, value, 1 + node2, mid + 1, end)
        
        tree[node] = tree[node2] + tree[1 + node2]
        
    init()
    
    for _ in range(m):
        q, l, r = map(int, input().split())
        if q & 1:
            print(f'{query(0, r - 1) - query(0, l - 1) + 1}\n')
        else:
            update(l - 1, 1)
            update(r, -1)
    
solve()