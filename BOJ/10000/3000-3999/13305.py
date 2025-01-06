n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = 0
minc = cost[0]
for x in range(n - 1):
    minc = min(minc, cost[x])
    result += minc * dist[x]
    
print(result)