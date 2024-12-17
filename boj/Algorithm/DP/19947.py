h, y = map(int, input().split())

cache = [[-1] * 200001 for _ in range(y + 1)]

def dp(pp, yy):
    if yy < 0 or pp > 200000:
        return 0

    if cache[yy][pp] != -1:
        return cache[yy][pp]
    
    result = pp
    for x, rate in [[1, 1.05], [3, 1.2], [5, 1.35]]:
        target = dp(int(pp * rate), yy - x)
        result = max(result, target)
    
    cache[yy][pp] = result
    return result

print(dp(h, y))