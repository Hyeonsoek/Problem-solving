def solve(x, n):
    names = [input() for _ in range(n)]
    earings = {name : [False, False] for name in names}
    
    for _ in range(2*n - 1):
        number, sign = input().split()
        earings[names[int(number)-1]][ord(sign) - ord('A')] = True
    
    for key, [left, right] in earings.items():
        if not left or not right:
            return f'{x} {key}'

c = 1
while True:
    n = int(input())
    if not n:
        break
    
    print(solve(c, n))
    c += 1