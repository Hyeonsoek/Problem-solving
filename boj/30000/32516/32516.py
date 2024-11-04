def solve():
    n = int(input())
    h = int(n / 2)
    t = input()
    
    result = 0
    for x in range(h):
        front = t[x]
        back = t[n - x - 1]
        
        if front == '?' and back == '?':
            result += 26
        elif '?' in [front, back]:
            result += 1
        else:
            if front != back:
                return 0
    
    return result

print(solve())
        

# a | b c ? | ? | ? q(6, c) q(7, b) | a