import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().strip()))[::-1]

    count = 0
    for i in range(n - 1):
        if arr[i] & 1:
            count += 1
        arr[i + 1] += (arr[i] + 1) // 2

    print(count)

solve()

# def solve():
#     input()
#     arr = input().strip('0\n')
#     print(arr.count('0') + (len(arr) > 1))