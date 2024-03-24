import sys
import bisect
input = sys.stdin.readline

class SqrtDecomposition:
    def __init__(self, n, arr):
        self.n = n
        self.arr = [0] + arr
        self.sqrt = 1500
        self.bucket = [[] for _ in range(n // self.sqrt + 2)]

        for x in range(1, n + 1):
            self.bucket[x // self.sqrt].append(arr[x-1])

        for bucket in self.bucket:
            bucket.sort()

    def update(self, index, k):
        group = index // self.sqrt
        self.bucket[group].remove(self.arr[index])
        target = bisect.bisect_left(self.bucket[group], k)
        self.bucket[group].insert(target, k)
        self.arr[index] = k

    def query(self, left, right, k):
        result = 0
        left_group = left // self.sqrt
        right_group = right // self.sqrt

        if left_group == right_group:
            for x in range(left, right + 1):
                result += self.arr[x] > k
            return result

        left_end = left_group * self.sqrt + self.sqrt
        for x in range(left, left_end):
            result += self.arr[x] > k

        right_start = right_group * self.sqrt
        for x in range(right_start, right + 1):
            result += self.arr[x] > k

        for x in range(left_group + 1, right_group):
            result += len(self.bucket[x]) - bisect.bisect_right(self.bucket[x], k)

        return result

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    decomposition = SqrtDecomposition(n, arr)

    qn = int(input())
    for _ in range(qn):
        q, *a = map(int, input().split())

        if q & 1:
            left, right, value = a
            print(decomposition.query(left, right, value))
        else:
            index, value = a
            decomposition.update(index, value)

solve()