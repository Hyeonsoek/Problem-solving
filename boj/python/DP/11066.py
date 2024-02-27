import sys
MAX = 100000000
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    arr = [*map(int, input().split())]
    A = [[0] * k for _ in range(k)]
    cache = [[-1] * k for _ in range(k)]
    prefix = [0] * (k + 1)

    for x in range(k):
        cache[x][x] = 0
        A[x][x] = x
        prefix[x + 1] = prefix[x] + arr[x]
    
    for interval in range(1, k):
        for start in range(k - interval):
            result = MAX
            end = start + interval
            section = prefix[end + 1] - prefix[start]
            for cut in range(A[start][end - 1], min(A[start + 1][end] + 1, end)):
                next_value = cache[start][cut] + cache[cut + 1][end] + section
                if result > next_value:
                    result = next_value
                    A[start][end] = cut
                
            cache[start][end] = result

    print(cache[0][k - 1])