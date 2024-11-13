# import sys
# input = sys.stdin.readline

# class Node:
#     def __init__(self, value = 0, count = 0) -> None:
#         self.value : int = value
#         self.count = 0

#     def propagate(self, lazy):
#         self.value += self.count * lazy
        
#     def __str__(self) -> str:
#         return f"[value] : {self.value}, [count] : {self.count}"

# def merge(a : Node, b : Node):
#     return Node(a.value + b.value, a.count + b.count)

# class SegTree:
#     def __init__(self, arr, n):
#         self.n = n
#         self.arr = arr
#         self.tree = [Node() for _ in range(4 * n)]
#         self.lazy = [0] * 4 * n

#         self.init(1, 1, n)

#     def init(self, node, start, end) -> Node:
#         if start == end:
#             self.tree[node].value = self.arr[start]
#             self.tree[node].count = 1
#             return self.tree[node]

#         mid = (start + end) >> 1
#         LL = self.init(node * 2, start, mid)
#         RR = self.init(node * 2 + 1, mid + 1, end)
#         self.tree[node] = merge(LL, RR)
#         return self.tree[node]

#     def propagate(self, node, start, end):
#         if self.lazy[node] != 0:
#             if start != end:
#                 self.lazy[node * 2] += self.lazy[node]
#                 self.lazy[node * 2 + 1] += self.lazy[node]
#             self.tree[node].propagate(self.lazy[node])
#             self.lazy[node] = 0

#     def update(self, value, left, right):
#         self._update(value, left, right, 1, 1, self.n)

#     def _update(self, value, left, right, node, start, end):
#         self.propagate(node, start, end)

#         if end < left or right < start:
#             return

#         if start <= left and right <= end:
#             self.lazy[node] = value
#             self.propagate(node, start, end)
#             return

#         mid = (start + end) >> 1
#         self._update(value, left, right, node * 2, start, mid)
#         self._update(value, left, right, node * 2 + 1, mid + 1, end)

#         self.tree[node] = merge(self.tree[node * 2], self.tree[node * 2 + 1])

#     def query(self, left, right):
#         return self._query(left, right, 1, 1, self.n)

#     def _query(self, left, right, node, start, end):
#         self.propagate(node, start, end)

#         if end < left or right < start:
#             return 0

#         if start <= left and right <= end:
#             return self.tree[node].value

#         mid = (start + end) >> 1
#         LL = self._query(left, right, node * 2, start, mid)
#         RR = self._query(left, right, node * 2 + 1, mid + 1, end)
#         return LL + RR


# def solve():
#     n = int(input())
#     m = n // 3
#     arr = [*map(int, input().split())]
#     color = [*input()]
    
#     A = [0] * (n + 1)
#     B = [0] * (n + 1)
#     C = [0] * (n + 1)
#     for x in range(n):
#         match color[x]:
#             case 'A':
#                 A[x] = arr[x]
#             case 'B':
#                 B[x] = arr[x]
#             case 'C':
#                 C[x] = arr[x]
    
#     segA = SegTree(A, n)
#     segB = SegTree(B, n)
    
#     print(*segA.tree, sep='\n')
#     print(sum(A))

# solve()