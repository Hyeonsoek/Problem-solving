from collections import defaultdict

def solve(n):
    cache = defaultdict(lambda : -1)
    
    def dynamic(size):
        if size < 3:
            return 0
        
        if 3 <= size <= 4:
            return 1
        
        if cache[size] != -1:
            return cache[size]
        
        n, r = divmod(size - 2, 3)
        result = 2 + (3 - r) * dynamic(n)
        if r == 1:
            result += dynamic(n + 1)
        elif r == 2:
            result += max(2 * dynamic(n + 1), dynamic(n) + dynamic(n + 2))
        
        cache[size] = result
        return result
    
    return dynamic(n)

print(solve(int(input())))