from sys import stdin
input = stdin.readline

N, M, L = map(int, input().split())
cut_lines = sorted([ int(input()) for _ in range(M) ])

for _ in range(N):
    target = int(input())
    
    answer = 0
    left, right = 2, L
    while left <= right:
        mid = (left + right) // 2
        
        current, count = 0, 0
        for x in range(M):
            if cut_lines[x] - current >= mid:
                count += 1
                current = cut_lines[x]

        if count < target or (count == target and L - current < mid):
            right = mid - 1
        else:
            left = mid + 1

    print(right)