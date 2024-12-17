import sys
input = sys.stdin.readline

def solve():
    people = set()
    queries = []
    qn = int(input())
    for _ in range(qn):
        a, b = input().split()
        people.add(a)
        people.add(b)
        queries.append((a, b))
    
    index = { name : x for x, name in enumerate(people) }
    
    count = [1] * len(people)
    parent = [x for x in range(len(people))]
    
    def find(u):
        if u == parent[u]:
            return u
        parent[u] = find(parent[u])
        return parent[u]
    
    for x in range(qn):
        a, b = queries[x]
        uu = find(index[a])
        vv = find(index[b])

        if uu != vv:
            parent[uu] = vv
            count[vv] += count[uu]
        
        print(count[vv])


t = int(input())
for _ in range(t):
    solve()