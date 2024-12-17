import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    books = []
    for x in range(m):
        int(input())
        books.append([*map(int, input().split())])
    
    for x in books:
        if x != sorted(x, reverse=True):
            return "No"
    
    return "Yes"

print(solve())