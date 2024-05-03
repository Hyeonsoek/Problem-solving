import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
cards = defaultdict(int)
for x in map(int, input().split()):
    cards[x] += 1

input()
print(*[cards[x] for x in map(int, input().split())])