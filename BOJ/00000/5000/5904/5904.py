def solve():
    n = int(input())
    
    nn = 0
    length = [0, 3]
    while n > length[-1]:
        nn += 1
        length.append(length[-1] * 2 + nn + 3)
    
    while nn >= 0 and not length[nn] < n <= length[nn] + nn + 3:
        if n > length[nn] + nn + 3:
            n -= length[nn] + nn + 3
        nn -= 1
    
    print('m' if length[nn] + 1 == n else 'o')
    
solve()