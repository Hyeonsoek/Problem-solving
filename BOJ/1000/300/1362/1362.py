index = 1
while True:
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break
    
    result = True
    while True:
        x, value = input().split()
        
        if x == '#':
            break
        
        if not result:
            continue
        
        value = int(value)
        if x == 'F':
            w += value
        else:
            w -= value
        
        if w <= 0:
            result = False
    
    if (o * .5) < w < o * 2:
        print(index, ":-)")
    elif w <= 0:
        print(index, "RIP")
    else:
        print(index, ":-(")

    index += 1