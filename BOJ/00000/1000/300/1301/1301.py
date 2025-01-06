def solve():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    defualt = [0] * n
    
    cache = {}
    cache[*defualt] = 1
    
    def dynamic(i, j, *args):
        if args in cache:
            return cache[args]
        
        if (i, j, *args) in cache:
            return cache[i, j, *args]

        result = 0
        count = list(args)
        for x in range(n):
            if i != x and j != x and count[x] > 0:
                count[x] -= 1
                result += dynamic(j, x, *count)
                count[x] += 1
        
        cache[i, j, *args] = result
        return result

    result = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                arr[i] -= 1
                arr[j] -= 1
                result += dynamic(i, j, *arr)
                arr[i] += 1
                arr[j] += 1
    
    print(result)

solve()