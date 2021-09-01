# stdin - 452ms
# input - 4840ms
# 시간차이 극심하다...
from sys import stdin

def eratosthenes():

	MAX = 1000001
	cache = [ 0 for _ in range(MAX) ]

	for y in range(2, MAX):
		if cache[y] == 0:
			for x in range(y*2, MAX, y):
				cache[x] = 1

	return cache

def goldbach(n):

	for x in range(3, n//2+1):
		if cache[n - x] == 0 and cache[x] == 0:
			return '{} = {} + {}'.format(n, x, n - x)

	return "Goldbach's conjecture is wrong."

cache = eratosthenes()

while True:
	 n = int(stdin.readline().strip())

	 if n == 0:
	 	break

	 print(goldbach(n))
