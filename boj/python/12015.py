import bisect

n = int(input())
array = list(map(int, input().split()))

answer = [array[0]]

def lower_bound(x):
    low, high = 0, len(answer) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if x > answer[mid]:
            low = mid + 1
        else:
            high = mid - 1
            
    return high + 1

for x in array[1:]:
    if answer[-1] < x:
        answer.append(x)
    else:
        index = lower_bound(x) #bisect.bisect_left(answer, x)
        answer[index] = x

print(len(answer))