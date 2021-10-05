def make_ternary(n):
    if n == 0:
        return "0"

    minus = True if n < 0 else False

    n = abs(n)
    ternary = ""
    while n > 0:
        n, mod = divmod(n, 3)
        ternary += str(mod)

    idx = 0
    ternary = list(map(int, list(ternary)))
    while idx < len(ternary):
        if ternary[idx] in [2, 3]:
            if ternary[idx] == 2:
                ternary[idx] = -1
            else:
                ternary[idx] = 0

            if idx + 1 < len(ternary):
                ternary[idx+1] += 1
            else:
                ternary.append(1)
        idx += 1

    if minus:
        for x in range(len(ternary)):
            ternary[x] = -ternary[x]

    ternary = ternary[::-1]
    answer = ""
    for x in range(len(ternary)):
        answer += 'T' if ternary[x] == -1 else str(ternary[x])
    return answer


print(make_ternary(int(input())))