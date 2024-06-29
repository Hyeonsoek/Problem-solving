import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    attack = list(map(int, input().split()))
    avoid = list(map(int, input().split()))
    rate = list(map(lambda x: float(x) * 10, input().split()))
    
    result = 0
    for x in range(n):
        result += max(int(attack[x] * rate[x]) // 10 - avoid[x], attack[x] - int(avoid[x] * rate[x]) // 10)
    
    print(result)
    
solve()