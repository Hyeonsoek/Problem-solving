def solve():
    n = int(input())
    nto1 = n * (n + 1) // 2
    an = [2, -1, 2]
    result = [1, 2]
    
    for x in range(3, n + 1):
        result.append(result[-1] + an[(x - 3) % 3])
        
    if sum(result) == nto1:
        print(n)
        print(*result, 1)
        return
    
    result = [1]
    for x in range(2, n + 1):
        result.append(result[-1] + an[(x-2) % 3])
    
    print(n)
    print(*result, 1)
    
solve()