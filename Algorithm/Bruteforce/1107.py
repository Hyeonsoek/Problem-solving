def solve():
    n, m = int(input()), int(input())
    broken = [False] * 10

    if m > 0:
        for x in list(map(int, input().split())):
            broken[x] = True

    def is_in_broken(num):
        for digit in num:
            if broken[int(digit)]:
                return False
        return True

    result = abs(100-n)
    for x in range(1000000):
        if is_in_broken(str(x)):
            result = min(result, len(str(x)) + abs(x-n))

    print(result)


solve()