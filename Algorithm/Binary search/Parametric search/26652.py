import sys
input = sys.stdin.readline

def tt(n, m, levels, counts):
    answer = -1
    max_lv = max(levels)
    left, right = 0, 10 ** 13
    
    for x in range(n):
        b2_4ac = ( 4 * (levels[x] * levels[x]) - 4 * levels[x] + 1 + 8 * counts[x] ) ** 0.5
        levels[x] = int((b2_4ac + 1) / 2)

    while left + 1 < right:
        result = 0
        mid = (left + right) // 2

        for x in range(n):
            result += max(0, mid - levels[x])
        
        if result <= m:
            answer = max(answer, mid)
            left = mid
        else:
            right = mid
    
    return answer if answer >= max_lv else -1

n, m = map(int, input().split())
levels = list(map(int, input().split()))
counts = list(map(int, input().split()))

print(tt(n, m, levels, counts))

# def ss(n, m, l, a):
#     maxLv=0
#     lv=[]
#     for i in range(n):
#         maxLv=max(maxLv,l[i])
#         lv.append( int( ( ( 4 * l[i] * (l[i] - 1) + 8 * a[i] + 1) ** .5 + 1) // 2 ) )

#     # print(lv)

#     def reqPotion(mid):
#         req=0
#         for i in range(n):
#             req+=max(0,mid-lv[i])
#         return req   

#     lo=0
#     hi=10**13
#     while lo+1<hi:
#         mid=(lo+hi)//2
#         if reqPotion(mid) <= m:
#             lo=mid
#         else:
#             hi=mid
#     return lo if lo>=maxLv else -1

# n, m = 3, 52
# levels = [29, 13, 36]
# counts = [20, 2, 55]

# print(tt(n, m, levels[:], counts[:]))
# print(ss(n, m, levels[:], counts[:]))

# import random

# while True:
#     n = random.randrange(3, 100)
#     m = random.randrange(0, 100)
#     levels = [ random.randrange(1, 100) for _ in range(n) ]
#     counts = [ random.randrange(0, 100) for _ in range(n) ]
    
#     t_result = tt(n, m, levels[:], counts[:])
#     s_result = ss(n, m, levels[:], counts[:])
    
#     if t_result != s_result:
#         if n <= 1000:
#             print("NO!")
#             print("---------------------------------------------------")
#             print("n, m =", n, m)
#             print("levels =", levels)
#             print("counts =", counts)
#             print("my result :", t_result)
#             print("answer :", s_result)
#             break