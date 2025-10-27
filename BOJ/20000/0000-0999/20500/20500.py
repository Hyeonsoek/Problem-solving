MOD = 1000000007
a = 0
for i in range(int(input()) - 1):
    a = (a * 2 + (-1 if i & 1 else 1)) % MOD
print(a)