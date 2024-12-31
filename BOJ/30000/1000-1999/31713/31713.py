t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    count = 0
    while True:
        y = b - 3 * a
        x = 4 * a - b
        
        if x < 0:
            count += 1
            a += 1
            
        if y < 0:
            count += 1
            b += 1
            
        if x >= 0 and y >= 0:
            break
        
    print(count)