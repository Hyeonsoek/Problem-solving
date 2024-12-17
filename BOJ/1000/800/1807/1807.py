def prefix(n):
    result = 0
    a = 9
    nn = n
    for x in range(1, len(str(n)) + 1):
        aa = min(a, nn)
        result += (x + 1) * aa
        nn -= a
        a *= 10
    result -= n // 4
    return result

def solve(k):
    low = 1
    high = 10 ** 15
    while low <= high:
        mid = (low + high) // 2
        t = prefix(mid)
        
        if t < k:
            low = mid + 1
        else:
            high = mid - 1
    
    l = len(str(low)) + (low % 4 > 0)
    k = l - 1 - (prefix(low) - k)
    
    if low % 4 == 0:
        print(str(low)[k])
    else:
        for x in range(10):
            string = str(low) + str(x)
            if int(string) % 4 == 0:
                print(string[k])
                break
    
while (i := int(input())) != 0:
    solve(i)