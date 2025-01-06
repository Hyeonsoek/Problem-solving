import sys
sys.setrecursionlimit(100000)

def solve():
    n = int(input())
    rice = [[*map(int, input().split())] for _ in range(n)]
    visited = [[False] * 10 for _ in range(n + 1)]
    result = [0] * n
    
    def dynamic(x, prev):
        if x == n:
            return True
        
        for xx in range(1, rice[x][0] + 1):
            value = rice[x][xx]
            if value != prev and not visited[x+1][value]:
                visited[x+1][value] = True
                result[x] = value
                if dynamic(x + 1, value):
                    return True
                
        return False

    print(*result, sep='\n') if dynamic(0, 0) else print(-1)
    
solve()