import math

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    
    result = 1
    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
        result += count * math.factorial(n - i - 1)
    
    print(result)

solve()