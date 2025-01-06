n = int(input())
arr = list(range(n))

def binary_search(value, left, right):
    mid = (left + right) // 2
    
    if arr[mid] == value:
        return 0
    elif value < arr[mid]:
        return 1 + binary_search(value, left, mid - 1)
    else:
        return 1 + binary_search(value, mid + 1, right)

def ternary_search(value, left, right):
    left_third = left + (right - left) // 3
    right_third = right - (right - left) // 3
    
    if arr[left_third] == value:
        return 0
    elif arr[right_third] == value:
        return 1
    elif value < arr[left_third]:
        return 2 + ternary_search(value, left, left_third - 1)
    elif value < arr[right_third]:
        return 2 + ternary_search(value, left_third + 1, right_third - 1)
    else:
        return 2 + ternary_search(value, right_third + 1, right)

result = [0, 0, 0]

for x in range(n):
    binary = binary_search(x, 0, n - 1)
    ternary = ternary_search(x, 0, n - 1)

    if binary < ternary:
        result[0] += 1
    elif binary == ternary:
        result[1] += 1
    else:
        result[2] += 1

print(*result, sep='\n')