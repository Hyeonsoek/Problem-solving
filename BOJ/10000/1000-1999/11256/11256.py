import sys
input = sys.stdin.readline

def solve():
    j, n = map(int, input().split())
    boxes = [tuple(map(int, input().split())) for _ in range(n)]
    boxes.sort(key=lambda x: x[0] * x[1], reverse=True)
    
    for i in range(n):
        if j <= 0:
            break
        j -= boxes[i][0] * boxes[i][1]
    
    print(i)

for _ in range(int(input())):
    solve()