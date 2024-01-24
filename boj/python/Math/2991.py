a, b, c, d = map(int, input().split())
p, m, n = map(int, input().split())

p1, p2 = p % (a + b), p % (c + d)
m1, m2 = m % (a + b), m % (c + d)
n1, n2 = n % (a + b), n % (c + d)

pp = (1 if 0 < p1 <= a else 0) + (1 if 0 < p2 <= c else 0)
mm = (1 if 0 < m1 <= a else 0) + (1 if 0 < m2 <= c else 0)
nn = (1 if 0 < n1 <= a else 0) + (1 if 0 < n2 <= c else 0)
print(pp)
print(mm)
print(nn)