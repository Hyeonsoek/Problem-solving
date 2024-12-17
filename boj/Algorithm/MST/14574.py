import math
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
infos = [ list(map(int, input().split())) for _ in range(n) ]

graph = [ ]
for front in range(n - 1):
    for back in range(front + 1, n):
        front_p, front_c = infos[front]
        back_p, back_c = infos[back]
         
        cost = math.floor( (front_c + back_c) / abs(back_p - front_p) )
        graph.append((cost, front, back))

parent = [ x for x in range(n) ]

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    u = find(u)
    v = find(v)
    
    if u == v:
        return False
    
    parent[u] = v
    return True

graph.sort(reverse = True)

MST = [ [] for _ in range(n) ]
rating, count = 0, 0
for cost, front, back in graph:
    if merge(front, back):
        MST[front].append(back)
        MST[back].append(front)
        
        rating += cost
        count += 1
        
        if count == n - 1:
            break

check = [False for _ in range(n)]

def post_order(vertex):
    check[vertex] = True
    sequence = []
    for next in MST[vertex]:
        if check[next] == False:
            next_sequence = post_order(next)
            for x in next_sequence:
                sequence.append(x)
                
            sequence.append([vertex + 1, next + 1])
            
    return sequence

sequence = post_order(parent[0])

print(rating)
for x in sequence:
    print(x[0], x[1])