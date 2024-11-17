import sys
input = sys.stdin.readline

def getstudent():
    name, *date = input().split()
    dd, mm, yy = map(int, date)
    return (yy, mm, dd), name

def solve():
    n = int(input())
    student = [getstudent() for _ in range(n)]
    print(max(student)[1])
    print(min(student)[1])

solve()