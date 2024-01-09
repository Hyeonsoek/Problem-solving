import math
n, m, k = map(int, input().split())

print(min(int(math.log(n, 2)), int(math.log(k, 2) + m)))