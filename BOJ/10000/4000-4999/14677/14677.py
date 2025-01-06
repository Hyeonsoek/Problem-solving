from collections import defaultdict
import sys
sys.setrecursionlimit(2000)

def solve():
    n = int(input())
    string = input()
    meal = 'BLD'

    cache = defaultdict(int)
    for x in range(3):
        cache['', x] = 0
    
    def dfs(node, time):
        if (node, time) in cache:
            return cache[node, time]
        
        result = 0
        nexttime = (time + 1) % 3
        if node[-1] == meal[time]:
            result = max(result, 1 + dfs(node[:-1], nexttime))
        
        if node[0] == meal[time]:
            result = max(result, 1 + dfs(node[1:], nexttime))
        
        cache[node, time] = result
        return result

    print(dfs(string, 0))

solve()