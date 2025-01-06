def solve():
    inputs = open(0).readlines()
    n, *arr = map(int, inputs[0].split())
    for x in inputs[1:]:
        for xx in map(int, x.split()):
            arr.append(xx)

    for x in range(n):
        arr[x] = int(''.join(reversed(str(arr[x]))))
        
    arr.sort()
    print(*arr, sep='\n')

solve()