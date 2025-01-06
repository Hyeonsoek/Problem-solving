from math import ceil

n, word = input().split()
n = int(n)

def get_func():
    if word == 'in':
        def _func(arr:list):
            values = [0] * n
            left = arr[:n//2][::-1]
            right = arr[n//2:][::-1]
            for x in range(n):
                values[x] = left.pop() if x & 1 else right.pop()
            return values
    
        return _func
    else:
        def _func(arr:list):
            values = [0] * n
            left = arr[:ceil(n/2)][::-1]
            right = arr[ceil(n/2):][::-1]
            for x in range(n):
                values[x] = right.pop() if x & 1 else left.pop()
            return values
    
        return _func

result = 1
func = get_func()
start = func(list(range(n)))
while start != list(range(n)):
    start = func(start)
    result += 1
    
print(result)