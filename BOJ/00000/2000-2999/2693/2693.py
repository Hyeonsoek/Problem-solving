import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    print(sorted(map(int, input().split()))[-3])