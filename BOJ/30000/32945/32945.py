import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = sorted([*map(int, input().split())], reverse=True)
    
    time = defaultdict(int)
    for i in range(n):
        time[i] += 1
        time[i + arr[i]] -= 1

    timeKeys = sorted(time.keys())    
    for i in range(1, len(timeKeys)):
        time[timeKeys[i]] += time[timeKeys[i - 1]]
    
    print(max(time.values()))

solve()