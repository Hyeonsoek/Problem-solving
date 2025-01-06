import sys

def solve(n):
    length = len(n)
    nn = int(n)
    
    result = [0] * length
    for x in range(1, length + 1):
        digits = str(nn * x).zfill(length)
        for interval in range(length):
            for i in range(length):
                if n[i] != digits[(i + interval) % length]:
                    break
            else:
                result[x - 1] = 1
                break
    
    print(f'{n} is', 'cyclic' if sum(result) == length else 'not cyclic')

for string in sys.stdin:
    solve(string.strip())