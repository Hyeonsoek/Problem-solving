a,b = map(int,input().split(' '))
ar = []

for i in range(a):
	newa = input()
	ar.append(newa)

ans = ""
cnt = []

for i in range(b):
	line = []
	for j in range(26):
		line.append(0)
	cnt.append(line)

for i in range(b):
	for j in range(a):
		cnt[i][ord(ar[j][i])-ord('A')] += 1

for i in cnt:
	ans += chr(i.index(max(i)) + ord('A'))

heming = 0
for i in ar:
	for j in range(b):
		if ans[j] != i[j]:
			heming+=1
print(ans)
print(heming)