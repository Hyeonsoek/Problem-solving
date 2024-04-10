import re
from collections import deque

T = int(input())

def make_answer(arr, reverse):
    ret = "["

    while arr:
        if reverse:
            ret += arr.pop()
        else:
            ret += arr.popleft()
        if arr:
            ret += ","

    return ret + "]"


for _ in range(T):
    rev = False
    error = False
    command = list(input())
    n = int(input())
    arrays = deque(re.findall('[0-9]+', input()))

    for c in command:
        if c == 'R':
            rev = not rev
        if c == 'D':
            if len(arrays) == 0:
                error = True
                break
            if rev:
                arrays.pop()
            else:
                arrays.popleft()

    if not error:
        print(make_answer(arrays, rev))
    else:
        print("error")