def equal(a, b, n):
    for x in range(n):
        if a[x] != b[x]:
            return False
    return True

def solve():
    n = int(input())
    arr = [*map(int, input().split())]

    count = 0
    while True:
        brr = [0] * n
        for x in range(n):
            for y in range(x + 1, n):
                brr[x] += arr[x] < arr[y]
                
        count += 1
        if not equal(arr, brr, n):
            arr = brr[:]
        else:
            break

    print(count)
    
solve()