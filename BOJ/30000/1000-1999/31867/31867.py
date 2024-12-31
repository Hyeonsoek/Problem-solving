n = int(input())
arr = list(map(int, input()))

odd = sum(map(lambda x: x%2, arr))
even = sum(map(lambda x: (x+1)%2, arr))

result = 0
if odd > even:
    result += 1
elif odd == even:
    result -= 1

print(result)