import sys
input = sys.stdin.readline

def add(dict: dict, value):
    if value in dict:
        dict[value] += 1
    else:
        dict[value] = 1

def remove(dict: dict, value):
    if value in dict:
        dict[value] -= 1
    
        if dict[value] == 0:
            del dict[value]

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    result = 0
    left, right = 1, n // m
    while left <= right:
        mid = (left + right) // 2
        
        start = 0
        index = 0
        count = 0
        record = {}
        while index < n:
            add(record, arr[index])
            if index >= start + mid:
                remove(record, arr[index - mid])
            
            if mid == len(record):
                count += 1
                start = index + 1
                record.clear()

            index += 1
            
        if count < m:
            right = mid - 1
        else:
            result = max(mid, result)
            left = mid + 1

    print(result)

solve()