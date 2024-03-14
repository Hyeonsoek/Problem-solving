cache = [[-1] * 31 for _ in range(31)]
cache[0][0] = 1


def dp(w, h):
    if cache[w][h] != -1:
        return cache[w][h]

    result = 0
    if w > 0:
        result += dp(w - 1, h + 1)

    if h > 0:
        result += dp(w, h - 1)
    cache[w][h] = result

    return result


dp(30, 0)

while n := int(input()):
    if n == 0:
        break
    print(cache[n][0])