def sovle():
    n, m, M, t, r = map(int, input().split())

    if m + t > M:
        return -1

    time = 0
    pulse = m
    result = 0
    while time < n:
        if pulse + t <= M:
            pulse += t
            time += 1
        else:
            pulse = max(pulse - r, m)
        result += 1

    return result

print(sovle())