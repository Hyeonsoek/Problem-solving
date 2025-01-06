def solve():
    def count(n):
        five = 0
        for x in range(1, 15):
            divisor = 5 ** x
            five += n // divisor
        
        two = 0
        for x in range(1, 32):
            divisor = 2 ** x
            two += n // divisor
            
        return five, two

    nn, mm = map(int, input().split())

    upperF, upperT = count(nn)
    lowerLF, lowerLT = count(mm)
    lowerRF, lowerRT = count(nn - mm)
    
    fives = upperF - (lowerLF + lowerRF)
    twos = upperT - (lowerLT + lowerRT)
    
    return min(fives, twos)

print(solve())