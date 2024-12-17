import sys
input = sys.stdin.readline
output = sys.stdout.write

def solve():
    array = []
    for i in range(int(input())):
        array.append(input().split() + [i])
    array.sort(key=lambda x: (int(x[0]), x[2]))

    for _year, _name, _ in array:
        output(f"{_year} {_name}\n")

solve()