import sys
input = sys.stdin.readline

n, q = map(int, input().split())

value = n
arr = [1] * n

for _ in range(q):
    q, *a = map(int, input().split())
    
    match q:
        case 1:
            index = a[0] - 1
            value -= arr[index]
            arr[index] = min(0, arr[index])
        case 2:
            index = a[0] - 1
            value += 1 - arr[index]
            arr[index] = max(1, arr[index])
        case 3:
            print(value)