import sys
from collections import defaultdict

def solve():
    n, Dest = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(n):
        S, E, D = map(int, input().split())
        graph[S].append((E, D))
    
    cache = {}
    def dynamic(start):
        if start > Dest:
            return sys.maxsize
        
        if start == Dest:
            return 0
        
        if start in cache:
            return cache[start]
        
        result = Dest - start
        for ss, (edgs) in graph.items():
            if start <= ss:
                for ee, dd in edgs:
                    if ee <= Dest:
                        result = min(result, dynamic(ee) + (ss - start) + dd)
        
        cache[start] = result
        return result

    print(dynamic(0))
    
solve()