import sys
input = sys.stdin.readline

def sovle():
    n, k = map(int, input().split())
    polygon = []
    for _ in range(n):
        pi = int(input())
        
        points = []
        circle = list(map(int, input().split()))
        for x in range(pi):
            points.append(circle[2*x] ** 2 + circle[2*x+1] ** 2)

        polygon.append(max(points))

    polygon.sort()
    print(f"{polygon[k-1]}.00")
    
sovle()