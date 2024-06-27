def solve():
    n = int(input())
    s = input()
    d, m = map(int, input().split())
    
    hyu = {'H':0, 'Y':0, 'U':0}
    nothyu = ['']
    for x in range(n):
        if s[x] in ['H', 'Y', 'U']:
            hyu[s[x]] += 1
            nothyu.append('')
        else:
            nothyu[-1] += s[x]
    
    nothyu = [x for x in nothyu if x]
    
    result = 0
    for x in nothyu:
        result += min(len(x) * d, m + d)
    
    result2 = min(hyu.values())
    
    print(result if result else "Nalmeok")
    print(result2 if result2 else "I love HanYang University")

solve()