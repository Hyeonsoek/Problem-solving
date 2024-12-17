from sys import stdin
input = stdin.readline

while True:
    edges = sorted(list(map(int, input().split())))
    
    if edges[0] == 0:
        break
    
    print("right" if edges[0] ** 2 + edges[1] ** 2 == edges[2] ** 2 else "wrong")