import sys
MOD = 10 ** 9 + 7
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    tree = [0] * 4 * n
    plazy = [0] * 4 * n
    mlazy = [1] * 4 * n
    
    def init(node = 1, start = 1, end = n):
        if start == end:
            tree[node] = arr[start - 1]
            return tree[node]

        mid = (start + end) >> 1
        LL = init(node * 2, start, mid)
        RR = init(node * 2 + 1, mid + 1, end)
        tree[node] = (LL + RR) % MOD
        return tree[node]

    def propagate(node, start, end):
        left = node << 1
        right = node << 1 | 1
        
        if mlazy[node] != 1:
            if start != end:
                mlazy[left] = (mlazy[left] * mlazy[node]) % MOD
                plazy[left] = (plazy[left] * mlazy[node]) % MOD
                
                mlazy[right] = (mlazy[right] * mlazy[node]) % MOD
                plazy[right] = (plazy[right] * mlazy[node]) % MOD
            
            tree[node] = (tree[node] * mlazy[node]) % MOD
            mlazy[node] = 1
        
        if plazy[node] != 0:
            if start != end:
                plazy[left] = (plazy[left] + plazy[node]) % MOD
                plazy[right] = (plazy[right] + plazy[node]) % MOD
            
            tree[node] = (tree[node] + plazy[node] * (end - start + 1)) % MOD
            plazy[node] = 0

    def query(left, right, node=1, start=1, end=n):
        propagate(node, start, end)
        
        if end < left or right < start:
            return 0
        
        if left <= start and end <= right:
            return tree[node]
        
        mid = (start + end) >> 1
        LL = query(left, right, node << 1, start, mid)
        RR = query(left, right, node << 1 | 1, mid + 1, end)
        return (LL + RR) % MOD


    def update(mult, plus, left, right, node=1, start=1, end=n):
        propagate(node, start, end)
        
        if end < left or right < start:
            return tree[node]

        if left <= start and end <= right:
            mlazy[node] *= mult
            plazy[node] += plus
            propagate(node, start, end)
            return tree[node]
        
        mid = (start + end) >> 1
        LL = update(mult, plus, left, right, node << 1, start, mid)
        RR = update(mult, plus, left, right, node << 1 | 1, mid + 1, end)
        tree[node] = (LL + RR) % MOD
        return tree[node]

    init()

    m = int(input())
    
    for _ in range(m):
        q, *values = map(int, input().split())
        
        if q == 4:
            s, e = values
            print(query(s, e))
        else:
            s, e, v = values
            match q:
                case 1:
                    update(1, v, s, e)
                case 2:
                    update(v, 0, s, e)
                case 3:
                    update(0, v, s, e)
        
solve()