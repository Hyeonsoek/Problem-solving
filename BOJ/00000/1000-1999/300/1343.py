import re

def solve():
    words = re.findall(r'[X]+|[.]+', input())

    result = ''
    for word in words:
        if 'X' in word:
            if len(word) % 2:
                return -1
            
            result += 'AAAA' * (len(word) // 4) + 'BB' * ((len(word) % 4) // 2)
        else:
            result += word

    return result

print(solve())