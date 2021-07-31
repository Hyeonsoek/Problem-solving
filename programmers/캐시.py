def solution(cacheSize, cities):
	answer = 0
	cache = []

	if cacheSize == 0:
		return len(cities) * 5

	for x in cities:
		x = x.lower()
		if cacheSize > len(cache):

			if x in cache :
				cache.remove(x)
				cache.append(x)
				answer += 1
			else :
				cache.append(x)
				answer += 5
		else:
			if x in cache:
				cache.remove(x)
				cache.append(x)
				answer += 1
			else :
				del cache[0]
				cache.append(x)
				answer += 5

	return answer