MOD = 10 ** 9 + 7

def pow(a, n):
    r = 1
    while n > 0:
        if n & 1:
            r = (a * r) % MOD
        a = (a * a) % MOD
        n >>= 1
    return r

def solve():
    string = input()
    m = len(string) >> 1
    
    count = 0
    for x in string:
        if x == '?':
            count += 1
    
    count = pow(2, count)
    
    for x in range(m):
        if string[x] != '?' and string[m+x] != '?' and string[x] != string[m+x]:
            return count
    
    result = [0] * m
    for x in range(m):
        if (string[x] == '?' and string[m+x] != '?') or\
            (string[x] != '?' and string[m+x] == '?'):
            result[x] += 1

        if string[x] == string[m+x] == '?':
            result[x] += 2
    
    r = 1
    for x in result:
        if x > 0:
            r = (r * x) % MOD
    
    return (count - r) % MOD
    
    
n = int(input())
for _ in range(n):
    print(solve())