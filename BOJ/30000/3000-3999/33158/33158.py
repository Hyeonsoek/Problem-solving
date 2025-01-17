import sys
sys.setrecursionlimit(220000)
D = 'DATA'
MIN = -sys.maxsize
input = sys.stdin.readline
output = sys.stdout.write

def solve():
    n, q = map(int, input().split())
    
    data = []
    for i in range(1, n + 1):
        string, weight = input().split()
        data.append((string, i, int(weight)))
    
    sorteddata = sorted(data)
    
    trie = {}
    revindexes = [0] * (n + 1)
    for i in range(1, n + 1):
        string, j, w = sorteddata[i-1]
        revindexes[j] = i
        head = trie
        for letter in string:
            head = head.setdefault(letter, {})
            if D in head:
                head[D][1] = i
            else:
                head[D] = [i, i]

    def search(string):
        head = trie
        for letter in string:
            if letter in head:
                head = head[letter]
            else:
                return [-1, -1]
        return head[D]

    tree = [[0, MIN] for _ in range(4 * n)]
    
    def init(node = 1, start = 1, end = n):
        if start == end:
            tree[node][0] = sorteddata[start - 1][1]
            tree[node][1] = sorteddata[start - 1][2]
            return tree[node]

        mid = (start + end) >> 1
        Li, Lw = init(node * 2, start, mid)
        Ri, Rw = init(node * 2 + 1, mid + 1, end)
        
        tree[node][1] = max(Lw, Rw)
        tree[node][0] = min(Li, Ri) if Lw == Rw else (Li if Lw > Rw else Ri)
        return tree[node]
    
    def query(left, right, node = 1, start = 1, end = n):
        if right < start or end < left:
            return [0, MIN]
        
        if left <= start and end <= right:
            return tree[node]
        
        mid = (start + end) >> 1
        Li, Lw = query(left, right, node * 2, start, mid)
        Ri, Rw = query(left, right, node * 2 + 1, mid + 1, end)
        
        Mw = max(Lw, Rw)
        Mi = min(Li, Ri) if Lw == Rw else (Li if Lw > Rw else Ri)
        return [Mi, Mw]
    
    def update(index, value, node = 1, start = 1, end = n):
        if index < start or end < index:
            return tree[node]
        
        if start == end:
            tree[node][1] += value
            return tree[node]
        
        mid = (start + end) >> 1
        Li, Lw = update(index, value, node * 2, start, mid)
        Ri, Rw = update(index, value, node * 2 + 1, mid + 1, end)
        
        tree[node][1] = max(Lw, Rw)
        tree[node][0] = min(Li, Ri) if Lw == Rw else (Li if Lw > Rw else Ri)
        return tree[node]
    
    init()

    for _ in range(q):
        t, d = input().split()
        left, right = search(t)
        
        if [-1, -1] != [left, right]:
            index, weight = query(left, right)
            output(f'{index}\n')
            update(revindexes[index], int(d))
        else:
            output(f'{-1}\n')

solve()