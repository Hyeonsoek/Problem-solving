a = int(input())
ar = []
for i in range(a):
	ar.append(int(input()))
ar.sort(reverse = True)

Max = -1
for i in range(a):
	temp = ar[i] * (i+1)
	if Max < temp:
		Max = temp

print(Max)