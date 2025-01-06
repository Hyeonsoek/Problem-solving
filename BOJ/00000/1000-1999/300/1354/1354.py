def solve():
    N, P, Q, X, Y = map(int, input().split())

    cache = {}

    def dynamic(index):
        if index <= 0:
            return 1

        if index in cache:
            return cache[index]

        t = int(index / P) - X
        p = int(index / Q) - Y
        cache[index] = dynamic(t) + dynamic(p)
        return cache[index]
    
    print(dynamic(N))

solve()