import sys
sys.setrecursionlimit(10000)
MAX = 10000001

def solve():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    def dynamic(start, mid, index):
        if index == n:
            return MAX if start == mid else 0
        
        result = cache[index][mid]
        if result != -1:
            return result
        
        result = MAX
        for x in range(3):
            if mid != x:
                result = min(result, arr[index][x] + dynamic(start, x, index + 1))
            
        cache[index][mid] = result
        return result

    answer = MAX
    for front in range(3):
        for mid in range(3):
            if front != mid:
                cache = [[-1] * 3 for _ in range(n)]
                answer = min(answer, arr[0][front] + arr[1][mid] + dynamic(front, mid, 2))
                
    print(answer)
    
solve()