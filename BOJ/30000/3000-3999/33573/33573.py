import sys, math
input = sys.stdin.readline

def solve():
    t = int(input())

    for _ in range(t):
        n = input()
        print("YES" if math.sqrt(int(n)).is_integer() and math.sqrt(int(n[::-1])).is_integer() else "NO")

solve()