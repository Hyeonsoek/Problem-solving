MAX = 1001

def solve():
    cache = [1] * MAX
    for value in range(1, MAX):
        for x in range(0, value):
            if (value - x) % 2 == 0:
                cache[value] += cache[(value - x) // 2]

    t = int(input())
    for _ in range(t):
        print(cache[int(input())])
    
solve()