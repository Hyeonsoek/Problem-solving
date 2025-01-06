import sys
from collections import Counter

n, m = map(int, input().split())
trees = Counter(list(map(int, sys.stdin.readline().split())))

answer = 0
low, high = 0, max(trees)

while low <= high:
	mid = (low + high) // 2

	my_tree = 0
	for tree, count in trees.items():
		my_tree += (tree - mid) * count if tree >= mid else 0

	if my_tree >= m:
		if mid > answer:
			answer = mid
		low = mid+1
		if my_tree == m:
			break
	else:
		high = mid-1

print(answer)