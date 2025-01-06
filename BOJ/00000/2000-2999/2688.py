cache = [[-1] * 10 for _ in range(66)]

for x in range(10):
    cache[0][x] = 1

def dp(nn, kk):
    if cache[nn][kk] != -1:
        return cache[nn][kk]
    
    result = 0
    for x in range(kk, 10):
        result += dp(nn - 1, x)
        
    cache[nn][kk] = result
    return result

dp(65, 0)

t = int(input())
for _ in range(t):
    print(cache[int(input())][0])