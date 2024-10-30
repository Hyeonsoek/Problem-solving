cash = int(input())
value = [*map(int, input().split())]

def BNP(cash, value):
    count = 0
    for x in range(14):
        if cash >= value[x]:
            count += cash // value[x]
            cash %= value[x]
            
    return cash + count * value[-1]

def TIMING(cash, value):
    count = 0
    for x in range(3, 14):
        if value[x-3] < value[x-2] < value[x-1]:
            cash += count * value[x]
            count = 0
        
        if value[x-3] > value[x-2] > value[x-1]:
            count += cash // value[x]
            cash %= value[x]
    
    return cash + count * value[-1]

bnp = BNP(cash, value)
timing = TIMING(cash, value)

print("SAMESAME" if bnp == timing else "BNP" if bnp > timing else "TIMING")