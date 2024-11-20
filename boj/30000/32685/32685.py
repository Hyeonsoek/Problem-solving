tobinary = lambda : f'{int(input()):b}'

a = tobinary()
b = tobinary()
c = tobinary()

m = max(4, len(a), len(b), len(c))

a = a.zfill(m)
b = b.zfill(m)
c = c.zfill(m)

print(str(int(a[m-4:m] + b[m-4:m] + c[m-4:m], 2)).zfill(4))