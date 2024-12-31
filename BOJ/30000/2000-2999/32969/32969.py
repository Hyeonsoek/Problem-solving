def solve():
    s = input()

    for i in ['social', 'history', 'language', 'literacy']:
        if i in s:
            return 'digital humanities'

    for i in ['bigdata', 'public', 'society']:
        if i in s:
            return 'public bigdata'

print(solve())