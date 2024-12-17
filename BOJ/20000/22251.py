def solve():
    digits = [
        set([1, 2, 3, 5, 6, 7]),
        set([3, 6]),
        set([1, 3, 4, 5, 7]),
        set([1, 3, 4, 6, 7]),
        set([2, 3, 4, 6]),
        set([1, 2, 4, 6, 7]),
        set([1, 2, 4, 5, 6, 7]),
        set([1, 3, 6]),
        set(range(1, 8)),
        set([1, 2, 3, 4, 6, 7])
    ]

    count = [[0] * 10 for _ in range(10)]

    for x in range(10):
        for y in range(10):
            count[x][y] = len(digits[x] ^ digits[y])

    n, k, p, x = map(int, input().split())

    x = list(str(x))

    while len(x) < k:
        x.insert(0, '0')

    result = set()

    def bruteforce(floor, pp, index):
        if 1 <= int(''.join(floor)) <= n:
            result.add(int(''.join(floor)))
        
        if index == k:
            return

        for y in range(10):
            digitvalue = int(floor[index])
            floor[index] = str(y)
            if pp >= count[digitvalue][y]:
                bruteforce(floor, pp - count[digitvalue][y], index+1)
            floor[index] = str(digitvalue)
                
    bruteforce(x, p, 0)

    print(len(result) - 1)

solve()