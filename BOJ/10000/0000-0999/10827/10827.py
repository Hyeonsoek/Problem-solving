a, b = input().split()
b = int(b)
aa, ab = a.split('.')

if int(aa) >= 1:
    aa = int(aa + ab)
    count = len(ab)
    result = str(aa ** b)
    result = result[:len(result) - count * b] + '.' + result[len(result) - count * b:]
    print(result)
else:
    aa = int(ab)
    count = len(ab)
    result = str(aa ** b)
    while len(result) < count * b:
        result = '0' + result
    
    print('0.' + result)