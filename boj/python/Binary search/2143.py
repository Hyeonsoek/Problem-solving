from bisect import bisect_left, bisect_right

T = int(input())
n = int(input())
array_a = list(map(int, input().split()))

m = int(input())
array_b = list(map(int, input().split()))

def make_prefix_sum(target_arr:list, len):
    prefix = target_arr[:]
    
    for x in range(1, len):
        prefix[x] += prefix[x-1]
        
    answer = prefix[:]
    for x in range(len):
        for y in range(x + 1, len):
            answer.append(prefix[y] - prefix[x])
        
    return sorted(answer)

prefix_a = make_prefix_sum(array_a, n)
prefix_b = make_prefix_sum(array_b, m)

answer = 0
for x in prefix_a:
    target = T - x
    left = bisect_left(prefix_b, target)
    right = bisect_right(prefix_b, target)
    
    if left >= len(prefix_b):
        continue
    
    answer += right - left
    
print(answer)