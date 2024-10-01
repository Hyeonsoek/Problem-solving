n = int(input())
minus = []
zero = []
plus = []

for _ in range(n):
    k = int(input())
    if k < 0:
        minus.append(k)
    elif k == 0:
        zero.append(k)
    else:
        plus.append(k)
    
minus.sort(reverse=True)
plus.sort()

result = 0
while len(minus) > 1:
    result += minus.pop() * minus.pop()

while len(minus) and len(zero):
    minus.pop()
    zero.pop()
    
if minus:
    result += minus.pop()

while len(plus) > 1:
    a = plus.pop()
    b = plus.pop()
    if a + b < a * b:
        result += a * b
    else:
        result += a
        plus.append(b)

if plus:
    result += plus.pop()

print(result)