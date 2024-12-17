import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    tree = [0] * (4 * n)
    
    def init(node, start, end):
        if start == end:
            tree[node] = 1
            return tree[node]
        
        mid = (start + end) // 2
        LL = init(node * 2, start, mid)
        RR = init(node * 2 + 1, mid + 1, end)
        tree[node] = LL + RR
        return tree[node]
    
    def update(node, start, end, index, value):
        if index < start or end < index:
            return tree[node]
        
        if start == end:
            tree[node] += value
            return tree[node]
        
        mid = (start + end) // 2
        LL = update(node * 2, start, mid, index, value)
        RR = update(node * 2 + 1, mid + 1, end, index, value)
        
        tree[node] = LL + RR
        return tree[node]
    
    def query(node, start, end, k):
        if start == end:
            return start
        
        LL = tree[node * 2]
        mid = (start + end) // 2
        
        if k <= LL:
            return query(node * 2, start, mid, k)
        else:
            return query(node * 2 + 1, mid + 1, end, k - LL)
    
    init(1, 1, n)
    
    result = []
    for x in range(n - 1, -1, -1):
        kth = x - arr[x] + 1
        
        if kth <= 0:
            print("NIE")
            return
        
        result.append(query(1, 1, n, kth))
        update(1, 1, n, result[-1], -1)
        
    print(*result[::-1], sep='\n')
    return
    
solve()