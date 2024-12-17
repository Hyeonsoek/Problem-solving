import sys
from math import log2
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = sorted([*map(int, input().split()), int(input())])[1:]
    
    result = []
    def postorder(node, h):
        if h < 0:
            return
        
        postorder(node - 2 ** (h - 1), h - 1)
        postorder(node + 2 ** (h - 1), h - 1)
        result.append(arr[node])
    
    postorder(n // 2, int(log2(n)))
    print(*result)

solve()