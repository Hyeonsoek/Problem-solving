n = int(input())
print(*sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x:x[1])[0])