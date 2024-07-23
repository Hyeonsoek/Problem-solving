d = int(input())
n, m, k = map(int, input().split())

result = []

nn = n // d
mm = m // d
kk = k // d

result.append((nn + mm + kk, k))

if k >= (nn + 1) * d - n + (mm + 1) * d - m:
    newm = (mm + 1) * d - m
    newn = (nn + 1) * d - n
    kknm = (k - newn - newm) // d
    result.append((2 + nn + mm + kknm, k - newn - newm))

if k >= (nn + 1) * d - n:
    newn = (nn + 1) * d - n
    kkn = (k - newn) // d
    result.append((1 + nn + mm + kkn, k - newn))

if k >= (mm + 1) * d - m:
    newm = (mm + 1) * d - m
    kkm = (k - newm) // d
    result.append((1 + nn + mm + kkm, k - newm))
    
result.sort()

print(result[-1][1])