def solve():
    n = int(input())
    cache = [0] * (n + 1)
    cache[0] = cache[2] = 1
    for i in range(4, n + 1, 2):
        for j in range(0, i + 1, 2):
            cache[i] += cache[j] * cache[i - j - 2]
            cache[i] %= 987654321
    print(cache[n])

solve()

# 카탈란수 공식
# import math
# a=int(input())
# print(math.comb(a,a//2)//(a//2+1)%987654321)