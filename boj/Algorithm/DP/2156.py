import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]
cache = [[-1] * 3 for _ in range(n)]

def dp(index, con):
    if index >= n:
        return 0
    
    if cache[index][con] != -1:
        return cache[index][con]
    
    if con < 2:
        cache[index][con] = max(cache[index][con], dp(index + 1, con + 1) + array[index])
    
    cache[index][con] = max(cache[index][con], dp(index + 1, 0))
    
    return cache[index][con]

print(dp(0, 0))