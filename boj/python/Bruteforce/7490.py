import re
from itertools import product

def operate(operations):
    regs = re.compile(r"[0-9]+|-|\+")
    strings = regs.findall("".join(operations))
    
    result = int(strings[0])
    for x in range(1, len(strings), 2):
        if strings[x] == "+":
            result += int(strings[x + 1])
        if strings[x] == "-":
            result -= int(strings[x + 1])
    
    return result == 0

t = int(input())
results = [[] for _ in range(10)]

for _ in range(t):
    n = int(input())
    
    if results[n]:
        for x in results[n]:
            print(x)
        print()
        continue
    
    array = [ str((x + 1) // 2) if x & 1 else "" for x in range(1, 2 * n) ]
    products = list(product(["+", "-", ""], repeat = n - 1))
    
    for p in products:
        temp = array[:]
        for x in range(1, 2 * n - 1, 2):
            temp[x] = p[x // 2]
        
        if operate(temp):
            for x in range(2 * n - 1):
                if temp[x] == "":
                    temp[x] = " "
            
            results[n].append("".join(temp))
    
    results[n].sort()
    
    for x in results[n]:
        print(x)
    print()