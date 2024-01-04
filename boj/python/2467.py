N = int(input())
number = sorted(list(map(int, input().split())))

MAX = 2*(10**9)+1

def two_pointer():
    minValue = MAX
    answer = [0, 0]

    front, back = 0, N-1

    while front < back:
        s = number[front] + number[back]

        if abs(s) < minValue:
            answer[0] = number[front]
            answer[1] = number[back]
            minValue = abs(s)

        if s < 0:
            front += 1
        elif s > 0:
            back -= 1
        else:
            break
        
    return answer

def binary_search():
    min_value = MAX
    answer = [0, 0]
    
    for x in range(0, N-1):
        front = number[x]
        low, high = x + 1, N - 1
        
        while low <= high:
            mid = (low + high) // 2
            mix = front + number[mid]
            
            if min_value > abs(mix):
                answer[0] = front
                answer[1] = number[mid]
                min_value = abs(mix)
                
            if mix < 0:
                low = mid + 1
            else:
                high = mid - 1
    
    return answer
    

# print(*two_pointer())
print(*binary_search())