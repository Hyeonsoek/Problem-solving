n, m = map(int, input().split())
narr = list(map(int, input().split()))
marr = sorted(list(map(int, input().split())))

result = sum(narr)

for x in range(m):
    if marr[x] > 0:
        result *= marr[x]
        
print(result)