def solve():
    MOD = 10007
    n = int(input())

    result = 1
    while n > 4:
        n -= 3
        result = (result * 3) % MOD

    return result * n % MOD
    
print(solve())