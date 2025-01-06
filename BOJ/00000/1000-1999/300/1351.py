n, p, q = map(int, input().split())

cache = {0:1}

def dynamic(nn):
    if nn in cache:
        return cache[nn]
    
    cache[nn] = dynamic(nn // p) + dynamic(nn // q)
    return cache[nn]
    
print(dynamic(n))