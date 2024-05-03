MAX = 100001

def sovle():
    isPrime = [1] * MAX
    isPrime[0] = isPrime[1] = 0
    for x in range(2, MAX):
        if isPrime[x]:
            for xx in range(2 * x, MAX, x):
                isPrime[xx] = 0
    
    primes = []
    cache = [-1] * MAX
    for x in range(2, MAX):
        if isPrime[x]:
            primes.append(x)
            cache[x] = 1
            value = x * x
            while value <= MAX:
                cache[value] = cache[value // x] + 1
                value *= x
    
    def dp(value):
        if cache[value] != -1:
            return cache[value]
        
        result = 0
        for prime in primes:
            if value % prime == 0:
                result = 1 + dp(value // prime)
                break
        
        cache[value] = result
        return result
    
    a, b = map(int, input().split())
    
    answer = 0
    for x in range(a, b + 1):
        count = dp(x)
        if isPrime[count]:
            answer += 1
        
    print(answer)
    
sovle()