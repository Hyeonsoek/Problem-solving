n = int(input())
arr = sorted(list(map(int, input().split())))
print(arr[(n-1)//2])