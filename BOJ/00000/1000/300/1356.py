def solve():
    s = list(map(int, input()))
    n = len(s)

    for x in range(1, n):
        left = 1
        for xx in range(x):
            left *= s[xx]
        
        right = 1
        for xx in range(x, n):
            right *= s[xx]
            
        if left == right:
            return "YES"
    
    return "NO"

print(solve())