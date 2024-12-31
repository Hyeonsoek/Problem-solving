def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    
    for x in range(1, n + 1):
        a, b = map(int, input().split())
        graph[x].append(a)
        graph[x].append(b)

    def DYNAMIC(K):
        cache = [[-1] * (n + 1) for _ in range(K + 1)]
        
        for x in range(1, n + 1):
            cache[K][x] = int(x == 1)
        
        def dynamic(x, k):
            if cache[k][x] != -1:
                return cache[k][x]

            result = int(x == 1)
            for next in graph[x]:
                value = dynamic(next, k + 1)
                if x == 1:
                    result = min(result, value)
                else:
                    result = max(result, value)

            cache[k][x] = result
            return result

        value = dynamic(1, 0)
        return value

    for k in range(10, 100):
        if DYNAMIC(k) == 0:
            return k

    return -1

print(solve())