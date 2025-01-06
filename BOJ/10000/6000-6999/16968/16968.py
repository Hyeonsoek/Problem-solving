form = input()

s = 10 if form[0] == 'd' else 26
for x in range(1, len(form)):
    if form[x] == 'd':
        s *= 9 if form[x-1] == 'd' else 10
    else:
        s *= 25 if form[x-1] == 'c' else 26

print(s)