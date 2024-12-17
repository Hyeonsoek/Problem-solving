import math

def solve():
    b = int(input())
    data = ''.join([input() for _ in range(math.ceil(b / 40))])
    ndata = []
    for x in range(b):
        ndata.append(f'{int(data[x*2:x*2+2], 16):08b}')
    
    index = 0
    result = ''
    while index < b:
        bit0 = ndata[index][0]
        bit7 = (0 if len(ndata[index]) < 2 else int(ndata[index][1:], 2))
        
        if bit0 == '0':
            value = 1 + bit7
            for x in range(value):
                index += 1
                result += f'{int(ndata[index], 2):02X}'
        else:
            index += 1
            count = 3 + bit7
            for x in range(count):
                result += f'{int(ndata[index], 2):02X}'
        
        index += 1

    count = math.ceil(len(result) / 80)
    print(len(result) // 2)
    for x in range(count):
        print(result[x * 80 : (x + 1) * 80])

for _ in range(int(input())):
    solve()