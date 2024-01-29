import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = 0
array = []
for x in range(n):
    a, b = map(int, input().split())
    array.append(a-b)
    
    result += b
    m -= 1000

array.sort(reverse=True)

for x in range(n):
    if m >= 4000 and result + array[x] > result:
        result += array[x]
        m -= 4000
    
print(result)