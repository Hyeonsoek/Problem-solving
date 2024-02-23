import sys
input = sys.stdin.readline
    
n = int(input())
names = [ input().rstrip() for _ in range(n) ]
    
head = list(range(n))
tail = list(range(n))
next = [-1] * n

for x in range(n-1):
    start, end = map(lambda x: int(x) - 1, input().split())
    next[tail[start]] = head[end]
    head[end] = head[start]
    tail[start] = tail[end]
    
start = head[0]
while head[start] != start:
    start = head[start]

while start != -1:
    print(names[start], end="")
    start = next[start]