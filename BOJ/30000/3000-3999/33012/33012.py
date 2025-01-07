def solve():
    n = int(input())

    data = [*range(1, n + 1)]
    
    s, e = 0, 0
    for i in range(n):
        if i & 1:
            s += data[i]
        else:
            e += data[i]
            
    p = -1 if n & 1 else 1
    i = n - 1
    res = max(s, e)
    while i > 0:
        ss = s - p
        ee = e + p
        if max(ss, ee) < res:
            s -= p
            e += p
            res = max(s, e)
            data[i], data[i-1] = data[i-1], data[i]
        i -= 2

    print(*data)
    print(max(s, e))

solve()

# def solve():
#     n = int(input())
#     k = (n + (n & 1)) >> 1
#     k -= k & 1
#     t = n - k

#     data = []
#     for i in range(1, t + 1):
#         data.append(i)

#     for i in range(t + 1, n, 2):
#         data.extend([i + 1, i])

#     s, e = 0, 0
#     for i in range(n):
#         if i & 1:
#             s += data[i]
#         else:
#             e += data[i]

#     print(*data)
#     print(max(s, e))

# solve()