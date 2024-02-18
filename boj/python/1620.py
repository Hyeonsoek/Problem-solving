import sys
input = sys.stdin.readline

n, m = map(int, input().split())
strings = [ input().rstrip() for _ in range(n) ]
book = { }
for x, string in enumerate(strings):
    book[str(x+1)] = string
    book[string] = x + 1

answer = [ book[input().rstrip()] for _ in range(m) ]
print(*answer, sep='\n')