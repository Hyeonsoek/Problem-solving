n, m = map(int, input().split())
s = set([input() for _ in range(n)])
print(sum([(1 if input() in s else 0) for _ in range(m)]))