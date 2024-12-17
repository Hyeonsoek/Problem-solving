def transform(x:str):
    return x.lower(), x

while True:
    n = int(input())
    if n == 0:
        break
    
    arr = sorted([ transform(input()) for _ in range(n) ])
    print(arr[0][1])