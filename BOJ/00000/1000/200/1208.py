from collections import defaultdict

def solve():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    def query(index, end, value):
        values = defaultdict(int)

        def _query(index, end, value):
            if index == end:
                values[value] += 1
                return

            _query(index + 1, end, value + arr[index])
            _query(index + 1, end, value)
        
        _query(index, end, value)
        return values
        
    left = query(0, n // 2, 0)
    right = query(n // 2, n, 0)

    result = 0
    for x in left.keys():
        value = s - x
        if value in right:
            result += right[value] * left[x]

    print(result - (1 if not s else 0))

solve()