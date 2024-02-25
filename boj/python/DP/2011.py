import sys
sys.setrecursionlimit(10000)

string = input()
length = len(string)
cache = [-1] * (length + 1)
cache[length] = 1

def dp(n):
    if cache[n] != -1:
        return cache[n]
    
    if string[n] == '0':
        return 0
    
    result = dp(n + 1)
    
    if n + 2 <= length and 10 <= int(string[n:n+2]) <= 26:
        result += dp(n + 2)
    
    cache[n] = result
    return result
    
print(dp(0) % 1000000)

# : 20236
# : 2
# : 2727
# : 1
# : 210
# : 1
# : 230
# : 0
# : 2
# : 1
# : 0
# : 0
# : 012
# : 0
# : 19126
# : 6
# : 111111111111111111111111111111
# : 346269