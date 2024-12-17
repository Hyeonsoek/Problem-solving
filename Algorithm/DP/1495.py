n, s, m = map(int, input().split())
musics = list(map(int, input().split()))
cache = [[-1] * (m + 1) for _ in range(n)]

def dp(index, volume):
    if volume < 0 or volume > m:
        return -2
    
    if index == n:
        return volume
    
    if cache[index][volume] != -1:
        return cache[index][volume]
    
    upper = dp(index + 1, volume + musics[index])
    lower = dp(index + 1, volume - musics[index])
    cache[index][volume] = max(upper, lower)
    return cache[index][volume]

result = dp(0, s)
print(-1 if result == -2 else result)