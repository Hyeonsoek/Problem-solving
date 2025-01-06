from collections import defaultdict

def solve():
    n = int(input())
    arr = input().split()
    
    prefix = defaultdict(int)
    
    for i in range(n):
        prefix[arr[i]] += 1
        if prefix[arr[i]] > 4:
            return i + 1
    
    return 0

print(solve())