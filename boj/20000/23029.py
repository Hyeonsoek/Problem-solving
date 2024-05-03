import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

def solve():
    n = int(input())
    food = [int(input()) for _ in range(n)]

    cache = [[-1] * 3 for _ in range(n)]

    cache[n-1][0] = food[n-1]
    cache[n-1][1] = food[n-1] // 2
    cache[n-1][2] = 0

    def dynamic(index, count):
        if cache[index][count] != -1:
            return cache[index][count]
        
        result = 0
        if count == 0:
            result = max(result, dynamic(index + 1, count + 1) + food[index])
        elif count == 1:
            result = max(result, dynamic(index + 1, count + 1) + food[index] // 2)
            
        result = max([result, dynamic(index + 1, 0)])
        
        cache[index][count] = result
        return result

    print(dynamic(0, 0))
    
solve()