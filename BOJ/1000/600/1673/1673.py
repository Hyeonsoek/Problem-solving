import sys

for i in sys.stdin.readlines():
    n, k = map(int, i.split())
    result = n
    stamp = n
    while stamp >= k:
        result += stamp // k
        stamp = stamp // k + stamp % k
    print(result)