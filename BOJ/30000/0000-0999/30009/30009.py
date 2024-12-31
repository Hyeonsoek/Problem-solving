n = int(input())
virus = [ input() for _ in range(n) ]
visited = [False] * n

def findk(string, x):
    result = 0
    length = min(len(string), len(virus[x]))
    for k in range(1, length + 1):
        if string[-k:] == virus[x][:k]:
            result = max(k, result)
    return result

def brute(string, nn):
    if nn == n:
        return len(string)
    else:
        result = 100
        for x in range(n):
            k = findk(string, x)
                
            if not visited[x] and (string == "" or k > 0):
                visited[x] = True
                result = min(result, brute(string + virus[x][k:], nn + 1))
                visited[x] = False
                
        return result

print(brute("", 0))