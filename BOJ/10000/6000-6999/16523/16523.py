import sys
sys.setrecursionlimit(1000000)
RATE = [1, 0.5, 0.25, 0.25, 0.25, 0.25]

def solve():
    n = int(input())
    prev = 0
    time = [0]
    cost = [0]
    for _ in range(n):
        D, C = map(int, input().split())
        time.append(prev := prev + D)
        cost.append(C)
        
    MAX = sum(cost)
    costPrev = [[0] * 6 for _ in range(n + 1)]
    
    for x in range(1, n + 1):
        for count in range(6):
            if x + count <= n and time[x + count - 1] - time[x - 1] < 120:
                result = 0
                for i in range(count + 1):
                    result += cost[x + i] * RATE[i]
                costPrev[x][count] = result
    
    cache = [[-1] * 6 for _ in range(n + 2)]
    for x in range(6):
        cache[n+1][x] = 0
    
    def dynamic(index, count):
        if cache[index][count] != -1:
            return cache[index][count]
        
        result = MAX
        for i in range(6):
            if costPrev[index][i] > 0:
                result = min(result, dynamic(index + i + 1, i) + costPrev[index][i])
        cache[index][count] = result
        return result

    print(f'{dynamic(1, 0):.2f}')

solve()