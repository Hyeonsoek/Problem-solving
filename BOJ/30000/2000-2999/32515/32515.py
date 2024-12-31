def solve():
    n = int(input())
    ss = input()
    sk = input()
    es = input()
    ek = input()
    
    result = ''
    for x in range(n):
        if ss[x] == es[x]:
            if sk[x] != ek[x]:
                return 'htg!'
            result += sk[x]
    return result

print(solve())
    

# 8
# HHVHVVHV
# 00100110
# HVHHHVVV
# 01100100 << 00100110