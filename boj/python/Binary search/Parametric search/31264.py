import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m, a = map(int, input().split())
array = sorted(list(map(int, input().split())))

low, high = 1, 100000
while low <= high:
    mid = (low + high) // 2
    # print('low, mid, high', low, mid, high)
    
    score, level = 0, mid
    for x in range(m):
        index = bisect_left(array, level)
        if index == 0:
            break
        
        if index == n and array[index - 1] < level:
            score += array[index - 1] * (m - x)
            break
        
        score += array[index - 1]
        level += array[index - 1]
        
    #     print('\t', score, level)
    
    # print("\tscore :", score)
    # print("-----------------------------")
        
    if score >= a:
        high = mid - 1
    else:
        low = mid + 1

print(high)

# array = [1, 5, 11, 16]

# print(bisect_left(array, 7)) #2
# print(bisect_left(array, 12)) #3
# print(bisect_left(array, 17)) #4
# print(bisect_left(array, 0)) #0

# print(bisect_right(array, 7)) #2
# print(bisect_right(array, 12)) #3
# print(bisect_right(array, 16)) #4
# print(bisect_right(array, 2)) #1
