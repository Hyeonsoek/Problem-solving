array = [1, 1, 0]
input_n = int(input())

for i in range(input_n - 1):
    array[(i + 2) % 3] = (array[i % 3] + array[(i + 1) % 3]) % 15746
    
print(array[input_n % 3])