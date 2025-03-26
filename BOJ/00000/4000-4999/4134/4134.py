import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        if n in [0, 1]:
            print(2)
        else:
            while True:
                if all(n % i for i in range(2, int(n ** 0.5) + 1)):
                    print(n)
                    break
                n += 1

solve()