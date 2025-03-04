import sys
input = sys.stdin.readline

m, n, L = map(int, input().split())
position = sorted(list(map(int, input().split())))

result = 0
for x in range(n):
    xx, yy = map(int, input().split())
    low, high = 0, m - 1
    while low <= high:
        mid = (low + high) // 2
        pos = position[mid]
        dist = abs(pos - xx) + yy
        
        if L < dist:
            if xx < pos:
                high = mid - 1
            else:
                low = mid + 1
        else:
            result += 1
            break
            
print(result)