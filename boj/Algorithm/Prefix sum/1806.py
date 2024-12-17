import sys
input = sys.stdin.readline

MAX = 987654321

n, s = map(int, input().split())
array = list(map(int, input().split()))

answer = MAX
value = array[0]
front, back = 0, 0

while front < n and back < n and front <= back:
    if value < s:
        back += 1
        if back < n:
            value += array[back]
    else:
        answer = min(answer, back - front + 1)
        value -= array[front]
        front += 1

print(0 if answer == MAX else answer)