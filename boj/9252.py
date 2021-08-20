A, B = list(input()), list(input())

LCS = [[-1] * (len(A)+1) for _ in range(len(B)+1)]

for i in range(len(B)+1):
	for j in range(len(A)+1):
		if i == 0 or j == 0:
			LCS[i][j] = 0
		elif B[i-1] == A[j-1]:
			LCS[i][j] = LCS[i-1][j-1] + 1
		else:
			LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

def find_LCS():
	
	LCSstring = ""
	sy, sx = len(B), len(A)

	while sy > 0 and sx > 0 and LCS[sy][sx] > 0:
		if LCS[sy][sx] == LCS[sy-1][sx]:
			sy -= 1
			continue

		if LCS[sy][sx] == LCS[sy][sx-1]:
			sx -= 1
			continue

		LCSstring += A[sx-1]
		sy -= 1
		sx -= 1

	return LCSstring

answer = find_LCS()[::-1]
print(len(answer))
print(answer)