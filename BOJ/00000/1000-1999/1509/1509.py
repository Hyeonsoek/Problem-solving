
def solve():
    string = input()
    
    n = len(string)
    isPalindrom = [[True] * n for _ in range(n)]
    
    for i in range(n):
        isPalindrom[i][i] = True
    
    for i in range(n - 1):
        isPalindrom[i][i + 1] = string[i] == string[i + 1]
    
    for i in range(2, n):
        for s in range(n - i):
            isPalindrom[s][s + i] = string[s] == string[s + i] and isPalindrom[s + 1][s + i - 1]
    
    cache = [0] * (n + 1)
    cache[1] = 1
    cache[2] = 1 + (isPalindrom[0][1] == False)
    for e in range(3, n + 1):
        cache[e] = 2501
        for s in reversed(range(e)):
            if isPalindrom[s][e - 1]:
                cache[e] = min(cache[e], cache[s] + 1)
    
    print(cache[n])

solve()