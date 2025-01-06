t = int(input())
for _ in range(t):
    n = int(input())
    squre = str(n * n)    
    count = len(str(n))
    print("YES" if int(squre[-count:]) == n else "NO")