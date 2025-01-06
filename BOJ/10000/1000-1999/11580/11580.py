import sys
INDEX = {'N':0, 'E':1, 'S':2, 'W':3}
DRX = [1, 0, -1, 0]
DRY = [0, 1, 0, -1]
input = sys.stdin.readline

def solve():
    n = int(input())
    query = input().strip()
    
    sx = sy = 0
    coords = set([(sx, sy)])
    for x in range(n):
        sx += DRX[INDEX[query[x]]]
        sy += DRY[INDEX[query[x]]]
        coords.add((sx, sy))
    
    print(len(coords))

solve()