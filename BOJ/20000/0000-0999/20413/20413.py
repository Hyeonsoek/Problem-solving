import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s, g, p, d = map(int, input().split())
    tier = list(input())
    
    result = [0]
    for x in range(n):
        match tier[x]:
            case 'B':
                result.append(s - result[-1] - 1)
            case 'S':
                result.append(g - result[-1] - 1)
            case 'G':
                result.append(p - result[-1] - 1)
            case 'P':
                result.append(d - result[-1] - 1)
            case 'D':
                result.append(d)
    
    print(sum(result))

solve()