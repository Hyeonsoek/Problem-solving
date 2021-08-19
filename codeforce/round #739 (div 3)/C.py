t = int(input())

cache = [2*x + 1 for x in range(31623)]

for _ in range(t):
	k = int(input())
	n = -1
	for x in range(len(cache)):
		if k > cache[x]:
			k -= cache[x]
		else :
			n = x
			break

	yy, xx = 0, n
	for _ in range(n+1):
		k -= 1
		if k == 0:
			break
		yy += 1

	if k == 0:
		print(yy+1, xx+1)
		continue

	for _ in range(n+1):
		k -= 1
		if k == 0:
			break
		xx -= 1

	if k == 0:
		print(yy, xx)
		continue