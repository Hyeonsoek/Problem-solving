def solve():
    plane = input()
    crypto = input()
    n = len(plane)
    
    key = [(ord(c) - ord(p) + 26) % 26 for p, c in zip(plane, crypto)]
    
    for x in range(n):
        if key[x] == 0:
            key[x] = 'Z'
        else:
            key[x] = chr(key[x] + 64)
    
    key = ''.join(key)
    for x in range(1, n + 1):
        if n % x == 0:
            string = ''.join(key[:x]) * (n // x)
            if string == key:
                print(key[:x])
                break

solve()