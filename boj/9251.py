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

print(LCS[len(B)][len(A)])