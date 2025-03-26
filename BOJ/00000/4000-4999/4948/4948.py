import sys
input = sys.stdin.readline
MAX = 123456 * 2 + 1

def solve():
    isprime = [1] * MAX
    isprime[1] = isprime[0] = 0
    for i in range(2, MAX):
        if isprime[i]:
            for j in range(i * i, MAX, i):
                isprime[j] = 0
    
    for i in range(2, MAX):
        isprime[i] += isprime[i - 1]
    
    while (n := int(input())):
        print(isprime[n * 2] - isprime[n])

solve()