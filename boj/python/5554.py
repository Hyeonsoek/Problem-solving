answer=0
for _ in range(4):
	s = int(input())
	answer += s
print(answer//60)
print(answer%60)