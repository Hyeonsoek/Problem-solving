def solve():
    s = input()
    n = len(s)
    
    def brute(before, index, nn, k):
        if k == 0:
            return 1 if before <= int(s[index:], 16) else 0
        
        count = 0
        for x in range(1, nn - k + 1):
            next = int(s[index : index + x], 16)
            if before <= next:
                count += brute(next, index + x, nn - x, k - 1)
        
        return count
    
    result = 0
    for x in range(n):
        result += brute(0, 0, n, x)
    
    print(result)

t = int(input())
for _ in range(t):
    solve()