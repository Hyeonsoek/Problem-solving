def solve():
    s = input()
    length = len(s)
    i = 0
    while i < length:
        if i + 2 <= length and s[i:i+2] in ['pi', 'ka']:
            i += 2
        elif i + 3 <= length and s[i:i+3] == 'chu':
            i += 3
        else:
            return 'NO'
    
    return 'YES'

print(solve())