import sys
input = sys.stdin.readline

def p(arr, m, k):
    return sum(arr[i] for i in range((m - 1) % k, m, k)) * 2

def solve():
    n, k = map(int, input().split())
    
    left = []
    right = []
    
    for _ in range(n):
        v = int(input())
        if v < 0:
            left.append(-v)
        else:
            right.append(v)
    
    left.sort()
    right.sort()
    
    print(p(left, len(left), k) + p(right, len(right), k))

solve()