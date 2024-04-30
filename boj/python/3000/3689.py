# ---wrong answer--- #
# ---File being written--- #

# def solve():
#     s, n = map(int, input().split())
#     arr = list(map(int, input().split()))

#     if len(set(arr)) == n and s >= n:
#         return s
    
#     sigma = (s + 1) * s // 2
    
#     prefix = [0, arr[0]]
#     for x in range(1, n):
#         prefix.append(prefix[-1] + arr[x])
    
#     count = 0
#     prefixSet = set()
#     for x in range(s):
#         prefixSet.add(arr[x])
#         if len(prefixSet) != x + 1:
#             break
        
#         for start in range(x + 1, n, s):
#             end = min(n, start + s)
#             value = prefix[end] - prefix[start]
#             if end - start < s and len(set(arr[start:end])) == end - start:
#                 pass
#             elif value != sigma:
#                 break
#         else:
#             count += 1
    
#     return count

# t = int(input())
# for _ in range(t):
#     print(solve())