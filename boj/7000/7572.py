N = int(input())

tengan = list(range(10))
twoelvgi = list(chr(x+65) for x in range(12))

cycle = []

idxgan, idxgi = 0, 0

while len(cycle) < 60:
	cycle.append(twoelvgi[idxgi] + str(tengan[idxgan]))

	idxgi += 1
	idxgan += 1

	if idxgi == 12:
		idxgi = 0
	if idxgan == 10:
		idxgan = 0

print(cycle[N%60-4])