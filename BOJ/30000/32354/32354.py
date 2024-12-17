import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    node = 1
    root = [0] * (n + 1)
    parent = [-1] * (n + 1)
    value = [0] * (n + 1)
    
    for x in range(1, n + 1):
        query = input().split()
        match query[0]:
            case 'pop':
                node = parent[node]
            case 'print':
                print(value[node])
                root[x] = node
            case 'restore':
                node = root[int(query[1])]
                root[x] = node
            case 'push':
                value[x] = value[node] + int(query[1])
                parent[x] = node
                root[x] = x
                node = x

solve()