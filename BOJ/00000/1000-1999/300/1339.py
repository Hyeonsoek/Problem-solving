from collections import defaultdict

n = int(input())
array = [input() for _ in range(n)]
weights = defaultdict(int)

for word in array:
    for digit, alphabet in enumerate(word[::-1]):
        weights[alphabet] += 10 ** digit

weight_list = sorted(list(weights.items()), key = lambda x : -x[1])
max_value = 9

result = 0
for _, value in weight_list:
    result += value * max_value
    max_value -= 1
    
print(result)