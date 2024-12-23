import sys

def solve(N, K, X, Q):
    tree = [0] * 4 * N
    
    def _update(node, value):
        tree[node] = 0 if not value else (1 if value > 0 else -1)
    
    def init(node=1, start=0, end=N-1):
        if start == end:
            _update(node, X[start])
            return tree[node]
    
        mid = (start + end) >> 1
        LL = init((node << 1), start, mid)
        RR = init((node << 1) | 1, mid + 1, end)
        tree[node] = LL * RR
        return tree[node]

    def update(index, value, node=1, start=0, end=N-1):
        if index < start or end < index:
            return tree[node]
        
        if start == end:
            _update(node, value)
            return tree[node]

        mid = (start + end) >> 1
        LL = update(index, value, (node << 1), start, mid)
        RR = update(index, value, (node << 1) | 1, mid + 1, end)
        tree[node] = LL * RR
        return tree[node]

    def query(left, right, node=1, start=0, end=N-1):
        if end < left or right < start:
            return 1
        
        if left <= start and end <= right:
            return tree[node]
        
        mid = (start + end) >> 1
        LL = query(left, right, (node << 1), start, mid)
        RR = query(left, right, (node << 1) | 1, mid + 1, end)
        return LL * RR

    init()
    
    result = []
    for x in range(K):
        q, i, j = Q[x]
        i = int(i)
        
        match q:
            case 'C':
                v = int(j)
                update(i - 1, v)
            case 'P':
                j = int(j)
                x = query(i - 1, j - 1)
                result.append('0' if not x else ('+' if x > 0 else '-'))
        
    print(*result, sep='')


input = sys.stdin.read().split()
index = 0

while index < len(input):
    N, K = map(int, input[index:index+2]); index += 2
    X = [*map(int, input[index:index+N])]; index += N
    Q = []
    for i in range(K):
        Q.append(input[index:index+3])
        index += 3
    solve(N, K, X, Q)