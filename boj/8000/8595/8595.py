import re

n = int(input())
arr = re.findall(r'[0-9]+', input())
print(sum(map(int, arr)))