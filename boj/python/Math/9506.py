import sys, math
input = sys.stdin.readline

while True:
    n = int(input())
    
    if n == -1:
        break
    
    result = []
    rev_result = []
    sqrt = int(math.sqrt(n)) + 1
    for x in range(1, sqrt):
        if n % x == 0:
            result.append(x)
            if n // x != n:
                rev_result.append(n // x)
    
    sum_re = sum(result) + sum(rev_result)
    if sum_re == n:
        print(n, "=", " + ".join(map(str, result + rev_result[::-1])))
    else:
        print(n, "is NOT perfect.")