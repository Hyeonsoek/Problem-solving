import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    string = input().strip()
    
    if sum(arr) < n:
        return 'No'
    
    if not (string[0] == string[n-1] == 'a'):
        return 'No'
    
    brr = [0] * 4
    for x in string:
        brr[ord(x) - ord('a')] += 1
    
    for x in range(4):
        if arr[x] < brr[x]:
            return 'No'
    
    for x in range(1, n):
        if string[x - 1] == string[x]:
            return 'No'
    
    return 'Yes'

print(solve())