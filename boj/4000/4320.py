while (value := int(input())) != 0:
    result = 1
    for x in range(2, 32):
        xroot = int(abs(value) ** (1 / x))
        
        if value == xroot ** x or value == (-xroot) ** x:
            result = max(result, x)
            
        if value == (xroot + 1) ** x or value == (-xroot-1) ** x:
            result = max(result, x)
    
    print(result)