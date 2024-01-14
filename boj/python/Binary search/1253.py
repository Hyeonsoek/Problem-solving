from bisect import bisect_left, bisect_right

n = int(input())
numbers = sorted(list(map(int, input().split())))

def solve():
    count = 0
    for x in range(n):
        for y in range(n):
            if x == y:
                continue
            
            target = numbers[x] - numbers[y]
            
            left = bisect_left(numbers, target)
            right = bisect_right(numbers, target)
            
            result = [idx for idx in range(left, right) if idx != x and idx != y]
            
            if result:
                count += 1
                break
            
    return count

print(solve())