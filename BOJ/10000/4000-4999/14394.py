from collections import Counter

def solve():
    current = Counter(list(input()))
    target = Counter(list(input()))
    
    result = 0
    for x in "YRGB*":
        result += abs(target[x] - current[x])
        
    print(result // 2)
    
solve()