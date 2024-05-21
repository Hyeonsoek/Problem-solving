# import sys
# input = sys.stdin.readline

# def solve():
#     n, q = map(int, input().split())
#     arr = list(map(int, input().split()))
#     tree = [0] * (4 * n)
    
#     def init(node = 1, start = 0, end = n-1):
#         if start == end:
#             tree[node] = arr[start-1]
#             return

#         node2 = node << 1
#         mid = (start + end) // 2
#         init(node2, start, mid)
#         init(node2 + 1, mid + 1, end)
        
#         tree[node] = tree[node2] + tree[node2]
    
#     def update(index, value, node = 1, start = 0, end = n - 1):
#         if index < start or end < index:
#             return
        
#         if start == end:
#             tree[node] += value
#             return

#         node2 = node << 1
#         mid = (start + end) // 2
#         update(index, value, node2, start, mid)
#         update(index, value, node2 + 1, mid + 1, end)
        
#         tree[node] = tree[node2] + tree[node2 + 1]

# 작성중