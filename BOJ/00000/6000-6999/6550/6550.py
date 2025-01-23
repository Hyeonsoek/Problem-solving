import sys

for i in sys.stdin:
    s, t = i.split()
    j = 0
    for k in t:
        if k == s[j]:
            j += 1
            if j == len(s):
                break
    print('Yes' if j == len(s) else 'No')