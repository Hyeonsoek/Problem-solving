MAX = 5000

def general_term(x, n):
    return 1 + (x - 8) * (n - 1) + 4 * n * (n - 1)
    
def solve():
    r1, c1, r2, c2 = map(int, input().split())
    
    digits = 0
    result = [[] for _ in range(r2 - r1 + 1)]
    for y in range(r1, r2 + 1):
        for x in range(c1, c2 + 1):
            index = max(abs(x), abs(y))
            length = 2 * index + 1
            value = (2 * index + 1) ** 2 ## at max point
            
            if y == index:
                value -= index - x
            elif x == -index:
                value -= length - 1
                value -= index - y
            elif y == -index:
                value -= 2 * (length - 1)
                value -= index + x
            elif x == index and y < index:
                value -= 3 * (length - 1)
                value -= index + y
            
            result[y - r1].append(value)
            digits = max(digits, len(str(value)))
            
    for x in result:
        print(" ".join(map(lambda value: str(value).rjust(digits, ' '), x)))
        
solve()