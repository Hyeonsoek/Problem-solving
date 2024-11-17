import sys

def solve(n):
    string = ['-'] * 3 ** n
    
    def dnq(start, end):
        if start + 1 == end:
            return
        
        leftMid = start + (end - start) // 3
        rightMid = start + 2 * (end - start) // 3
        dnq(start, leftMid)
        dnq(rightMid, end)
        
        for x in range(leftMid, rightMid):
            string[x] = ' '
    
    dnq(0, 3 ** n)
    return ''.join(string)

for x in sys.stdin:
    print(solve(int(x)))