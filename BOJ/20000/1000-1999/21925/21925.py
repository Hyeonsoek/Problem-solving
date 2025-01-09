import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]

    left = 0
    count = 0
    result = 0
    for right in range(2, n + 1, 2):
        start = left
        end = right - 1
        while start < end:
            if arr[start] != arr[end]:
                break
            start += 1
            end -= 1
        else:
            count += right - left
            left = right
            result += 1
    
    print(result if count == n else -1)
    
solve()