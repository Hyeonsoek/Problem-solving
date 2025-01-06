MAX = 10001
p = [1] * MAX
prime = []
for i in range(2, MAX):
    if p[i]:
        prime.append(i)
        for j in range(i * i, MAX, i):
            p[j] = 0

m = len(prime)
mprime = set()
for i in range(1, m):
    mprime.add(prime[i] * prime[i - 1])

n = int(input()) + 1
while n not in mprime:
    n += 1

print(n)