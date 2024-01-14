n = int(input())
array_L = list(map(int, input().split()))
array_R = list(map(int, input().split()))

modula_value = 2 ** 64
def parametric(x):
    value = x
    for index in range(n):
        l = array_L[index]
        r = array_R[index]
        
        if l <= x <= r:
            value ^= (((x | l) + (x & r) * (l ^ r)) % modula_value)
    
    return value >= 0x0123456789ABCDEF
            
answer = 0
low, high = 0, 10 ** 18

while low <= high:
    mid = (low + high) // 2
    
    first = parametric(mid)
    second = parametric(mid + 1)
    
    if not first:
        if second:
            answer = mid
            break
        low = mid + 1
    else:
        high = mid - 1

print(answer)