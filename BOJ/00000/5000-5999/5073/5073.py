import sys

for i in sys.stdin:
    a, b, c = sorted(map(int, i.split()))
    if a == b == c == 0:
        break
    
    if a + b <= c:
        print('Invalid')
    else:
        if a == b == c:
            print('Equilateral')
        elif a == b or b == c or c == a:
            print('Isosceles')
        else:
            print('Scalene')