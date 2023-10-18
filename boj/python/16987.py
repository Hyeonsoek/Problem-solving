n = int(input())
eggs = [ list(map(int, input().split())) for _ in range(n) ]

def brute(pos : int, deggs : list):
    # print(pos, deggs)
    if pos == n:
        return sum(map(lambda x: 0 if x[0] > 0 else 1, deggs))
    else:
        result = -987654321
        
        if deggs[pos][0] > 0:
            for x in range(n):
                if x != pos and deggs[x][0] > 0:
                    deggs[pos][0] -= deggs[x][1]
                    deggs[x][0] -= deggs[pos][1]
                    result = max(result, brute(pos + 1, deggs[:]))
                    deggs[pos][0] += deggs[x][1]
                    deggs[x][0] += deggs[pos][1]
        
        if result == -987654321:
            result = max(result, brute(pos+1, deggs))
        
        return result
    
print(brute(0, eggs))