import sys
from collections import defaultdict
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        self.tree = [0] * (2*n)

        for x in range(n):
            self.tree[x+n] = arr[x]

        for x in range(n-1, 0, -1):
            self.tree[x] = self.tree[x << 1] + self.tree[x << 1 | 1]

    def update(self, index, value):
        self.tree[index + self.n] = value

        index += self.n
        while index > 1:
            index >>= 1
            self.tree[index] = self.tree[index << 1] + self.tree[index << 1 | 1]

    def query(self, left, right):
        result = 0

        left += self.n
        right += self.n

        while left < right:
            if left & 1:
                result += self.tree[left]
                left += 1

            if right & 1:
                right -= 1
                result += self.tree[right]

            left >>= 1
            right >>= 1

        return result

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    tree = SegmentTree(n, arr)
    qn = int(input())
    query_1 = []
    query_2 = defaultdict(list)

    count = 0
    for x in range(qn):
        q, *a = map(int, input().split())

        if q & 1:
            query_1.append(a)
        else:
            k, left, right = a
            query_2[k].append((left, right, count))
            count += 1

    result = [0] * count
    for x, (index, value) in enumerate(query_1):
        for left, right, count in query_2[x]:
            result[count] = tree.query(left-1, right)
        tree.update(index-1, value)

    for left, right, count in query_2[len(query_1)]:
        result[count] = tree.query(left-1, right)

    print(*result, sep='\n')

solve()