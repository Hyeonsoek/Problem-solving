import heapq, sys
MAX = 70
input = sys.stdin.readline

def less(left, right):
    if sum(left) != sum(right):
        return sum(left) < sum(right)

    for x in range(4):
        if left[x] < right[x]:
            return True
        elif left[x] > right[x]:
            return False
    return False

def solve():
    queue = [([0] * 5, 0)]
    buttons = [60, 10, -10, 1, -1]
    dicts = {x: [61] * 5 for x in range(MAX)}
    dicts[0] = [0] * 5

    while queue:
        counts, minuts = heapq.heappop(queue)

        if less(dicts[minuts], counts):
            continue

        for x in range(5):
            next = minuts + buttons[x]
            next_counts = counts[:]
            next_counts[x] += 1
            if 0 <= next < MAX and less(next_counts, dicts[next]):
                heapq.heappush(queue, (next_counts, next))
                dicts[next] = next_counts[:]

    t = int(input())
    for _ in range(t):
        nn = int(input())
        result = dicts[nn % 60][:]
        result[0] += nn//60
        print(*result)

solve()