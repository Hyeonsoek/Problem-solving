n = int(input())
string = list(input())
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    
    result = 0
    for cut in range(l, r):
        count = 0
        upper = string[l-1:cut][::-1]
        lower = string[cut:r:]
        for x in range(min(len(upper), len(lower))):
            if upper[x] == lower[x]:
                count += 1
        result = max(result, count)
    
    print(result)