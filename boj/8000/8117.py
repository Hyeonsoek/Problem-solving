import sys
input = sys.stdin.readline

def solve():
    arr = []
    while True:
        n = int(input())
        if not n:
            break
        
        arr.append(n)
        
    arr.sort()

    for x in range(2, len(arr)):
        if arr[x-2] + arr[x-1] > arr[x]:
            print(arr[x-2], arr[x-1], arr[x])
            return
    
    print("NIE")

solve()