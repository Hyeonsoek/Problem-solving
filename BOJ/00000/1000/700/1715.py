import sys
import heapq

N = int(sys.stdin.readline())
cards = sorted([ int(sys.stdin.readline()) for _ in range(N) ])

answer = 0

while len(cards) > 1:
	a = heapq.heappop(cards)
	b = heapq.heappop(cards)
	answer += a+b
	heapq.heappush(cards, a+b)

print(answer)