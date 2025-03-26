import sys, math
input = sys.stdin.readline

def solve():
    n = int(input())
    height = [int(input()) for _ in range(n)]
    height.sort()
    
    diff = [height[i + 1] - height[i] for i in range(n - 1)]
    gcd = math.gcd(*diff)
    
    print((sum(diff) // gcd) - n + 1)

solve()