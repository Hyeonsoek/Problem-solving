MAX = 1000001

def sovle(k):
    result = []
    isPrime = [0] * MAX
    for x in range(2, MAX):
        if isPrime[x] == 0:
            while k % x == 0:
                result.append(x)
                k //= x
            
            if k == 1:
                break
            
            for y in range(2 * x , MAX, x):
                isPrime[y] = 1

    if k == 1:
        print(len(result))
        print(*result)
    else:
        print(len(result) + 1)
        print(*result, k)
        
sovle(int(input()))