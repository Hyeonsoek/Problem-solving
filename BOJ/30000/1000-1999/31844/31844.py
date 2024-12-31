s = input()
r = s.find('@')
b = s.find('#')
t = s.find('!')

if r < b < t or t < b < r:
    print(abs(r - t)-1)
else:
    print(-1)