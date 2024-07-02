n, m = map(int, input().split())

if n >= 3:
    if m <= 4:
        print(m)
    elif m == 5:
        print(4)
    else:
        print(m - 2)
elif n == 2:
    if m <= 2:
        print(1)
    else:
        result = (m - 1) // 2 + 1
        print(result if result <= 4 else 4)
else:
    print(1)