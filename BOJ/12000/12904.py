s = input()
t = list(input())

count = len(t) - len(s)

for _ in range(count):
    top = t.pop()
    if top == 'B':
        t = t[::-1]
    
print(1 if s == ''.join(t) else 0)