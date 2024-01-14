from sys import stdin
input = stdin.readline

n = int(input())

min_cache = [ 0 ] * 3
max_cache = [ 0 ] * 3 

for _ in range(n):
    floor = list(map(int, input().split()))
    
    left_min = min(min_cache[:2])
    left_max = max(max_cache[:2])
    
    middle_min = min(min_cache)
    middle_max = max(max_cache)
    
    right_min = min(min_cache[1:])
    right_max = max(max_cache[1:])
    
    min_cache[0] = floor[0] + left_min
    max_cache[0] = floor[0] + left_max
    
    min_cache[1] = floor[1] + middle_min
    max_cache[1] = floor[1] + middle_max
    
    min_cache[2] = floor[2] + right_min
    max_cache[2] = floor[2] + right_max

print(max(max_cache), min(min_cache))