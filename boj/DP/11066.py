import sys
MAX = 100000000
input = sys.stdin.readline

def s():
        k = int(input())
        arr = [*map(int, input().split())]
        A = [[0] * (k+1) for _ in range(k+1)]
        cache = [[0] * (k+1) for _ in range(k+1)]
        prefix = [0]
    
        for x in range(k):
            A[x][x] = x
            prefix.append(prefix[-1] + arr[x])
        
        for interval in range(1, k):
            for start in range(k - interval):
                result = MAX
                end = start + interval
                
                for cut in range(A[start][end - 1], A[start + 1][end] + 1):
                    next_value = cache[start][cut] + cache[cut + 1][end] + prefix[end + 1] - prefix[start]
                    if result > next_value:
                        result = next_value
                        A[start][end] = cut
                    
                cache[start][end] = result
    
        print(cache[0][k - 1])

t = int(input())
for _ in range(t):
    s()