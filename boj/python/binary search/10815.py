n = int(input())
array = sorted(list(map(int, input().split())))

m = int(input())
search = list(map(int, input().split()))

def find(x):
    low, high = 0, n - 1
    
    while high >= low:
        mid = (low + high) // 2
        if array[mid] == x:
            return True
        elif array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
    
    return False

for x in search:
    print(1 if find(x) else 0, end=' ')