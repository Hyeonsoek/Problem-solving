import sys
input = sys.stdin.readline
MAX_POW = 19

m = int(input()[:-1])
fx = [[0 for _ in range(MAX_POW)] for _ in range(m + 1) ]

for idx, value in enumerate(list(map(int, input().split()))):
    fx[idx + 1][0] = value

for count in range(1, MAX_POW):
    for num in range(1, m + 1):
        fx[num][count] = fx[ fx[num][count - 1] ][ count - 1 ]
        
q = int(input()[:-1])
for _ in range(q):
    n, x = map(int, input().split())
    
    for count in range(MAX_POW - 1, -1, -1):
        if n >= (1 << count):
            n -= (1 << count)
            x = fx[x][count]
    
    print(x)