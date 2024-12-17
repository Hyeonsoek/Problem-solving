def get_mid(start, end):
	check = [0, 0, 0]
	check[start] = 1
	check[end] = 1

	for i in range(3):
		if check[i] == 0:
			return i

def hanoi(start, end, n):
	if n == 1:
		print(start+1, end+1)
	else:
		mid = get_mid(start, end)
		hanoi(start, mid, n-1)
		print(start+1, end+1)
		hanoi(mid, end, n-1)

n = int(input())
print(2**n - 1)
if n <= 20:
	hanoi(0, 2, n)