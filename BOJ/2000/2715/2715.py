def solve():
    n, *arr = map(int, input().split())
    
    result = []
    index = n - 1
    while arr:
        if arr[index] == index + 1:
            arr.pop()
            index -= 1
            continue
            
        if arr[0] == -(index + 1):
            result.append(index + 1)
            arr = [ -x for x in arr[::-1] ]
            continue
            
        for x, value in enumerate(arr):
            if abs(value) == index + 1:
                result.append(x + 1)
                arr = [ -x for x in reversed(arr[:x+1]) ] + arr[x+1:]
                break
    
    print(len(result), *result)

for _ in range(int(input())):
    solve()