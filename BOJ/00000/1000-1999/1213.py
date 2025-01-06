from collections import Counter

def solve():
    s = input()
    n = len(s)
    characters = dict(Counter(s))

    target = ''
    for key, value in characters.items():
        if value & 1:
            target += key
            
    if (n & 1 and len(target) > 1) or (not n & 1 and target):
        return "I'm Sorry Hansoo"
    
    result = ''
    keys = sorted(characters.keys())
    for key in keys:
        result += key * (characters[key] // 2)
    return result + target + result[::-1]

print(solve())