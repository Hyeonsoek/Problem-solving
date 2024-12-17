MOD = 1000000007

def sovle():
    p, c, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    d = [0]
    for x in range(1, p):
        d.append(arr[x] - arr[x-1])
    
    dp = 0
    for x in range(1, p):
        dp += -(c ** x) * d[-x]
        
    d.append(abs(dp) % MOD)
    
    for x in range(p + 1, k+1):
        value = abs((c ** p) * d[x - p]) % MOD
        d.append(value)
    
    print(d[-1])

sovle()