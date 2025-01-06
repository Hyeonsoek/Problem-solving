import math, sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    sqrt = int(n ** .5)
    
    arr = [0] * n
    bucket = [0] * (n // sqrt + 1)
    
    def query(left, right):
        result = 0
        
        while left < right and left % sqrt != 0:
            arr[left] += 1
            result += arr[left]
            left += 1
        
        if right < n:
            while left < right and right % sqrt != 0:
                right -= 1
                arr[right] += 1
                result += arr[right]
        
        left = math.ceil(left / sqrt)
        right = math.ceil(right / sqrt)
        for x in range(left, right):
            bucket[x] += 1
            result += bucket[x]

        return result

    for _ in range(m):
        count, start = map(int, input().split())
        print(query(start - 1, start + count - 1))

solve()