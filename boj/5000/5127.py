import sys
input = sys.stdin.readline

def solve():
    d, n = map(int, input().split())
    arr = list(map(int, input().split())) + [1]
    for x in reversed(range(d-1)):
        arr[x] *= arr[x+1]
    
    worths = []
    for _ in range(n):
        worth = 0
        values = list(map(int, input().split()))
        for x in range(d):
            worth += values[x] * arr[x]
        worths.append(worth)
    
    return max(worths) - min(worths)
    

k = int(input())
for xx in range(1, k + 1):
    print(f"Data Set {xx}:\n{solve()}")
    if xx < k:
        print()
        
'''
혹시나 문제를 이해못했다면...
0. [i] 지폐 1개 == [i+1] 지폐 arr[i]개
1. 뒤쪽이 가장 낮은 가치의 지폐이다
'''