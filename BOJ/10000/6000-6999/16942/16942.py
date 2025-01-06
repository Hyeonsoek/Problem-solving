def solve():
    string = input()
    n = len(string)
    cache = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if string[i] == string[j] and (j - i) & 1:
                cache[i] = max(cache[i], cache[j] + 1)
    
    print(max(cache))

solve()