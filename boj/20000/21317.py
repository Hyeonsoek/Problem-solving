MAX = 100000

def solve():
    n = int(input())
    costs = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        costs.append((a, b))
    k = int(input())
    
    cache = [[-1] * n for _ in range(2)]
    def dp(node, count):
        if node == n - 1:
            return 0
            
        if cache[count][node] != -1:
            return cache[count][node]
        
        result = MAX
        
        if node + 1 <= n - 1:
            one = dp(node + 1, count) + costs[node][0]
            result = min(result, one)
            
        if node + 2 <= n - 1:
            two = dp(node + 2, count) + costs[node][1]
            result = min(result, two)
        
        if count > 0 and node + 3 <= n - 1:
            three = dp(node + 3, count - 1) + k
            result = min(result, three)

        cache[count][node] = result
        return result
    
    print(dp(0, 1))
    
solve()