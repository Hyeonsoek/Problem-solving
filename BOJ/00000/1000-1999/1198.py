from itertools import combinations

n = int(input())
coords = []
for _ in range(n):
    a, b = map(int, input().split())
    coords.append((a, b))

def dist(a, b):
    ax, ay = a
    bx, by = b
    return ((ax - bx) ** 2 + (ay - by) ** 2) ** .5

def area(a, b, c):
    ab, bc, ca = dist(a, b), dist(b, c), dist(a, c)
    s = (ab + bc + ca) / 2
    return s * (s - ab) * (s - bc) * (s - ca)

result = 0    
for comb in combinations(coords, 3):
    result = max(result, area(*comb))
    
print(result ** .5)