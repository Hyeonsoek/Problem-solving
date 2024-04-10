from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
no_hear = set(input()[:-1] for _ in range(n))
no_see = set(input()[:-1] for _ in range(m))

no_hear_and_see = sorted(list(no_hear & no_see))

print(len(no_hear_and_see))
for x in no_hear_and_see:
    print(x)