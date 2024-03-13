import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    a = sum([int(input()) for _ in range(n)])
    print("+" if a > 0 else ('-' if a < 0 else a))