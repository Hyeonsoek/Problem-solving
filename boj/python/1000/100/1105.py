def solve(L, R):
    count = 0
    
    if len(L) != len(R):
        return 0
    
    for x in range(len(L)):
        if L[x] == R[x] and L[x] == '8':
            count += 1
        elif L[x] != R[x]:
            break

    return count

L, R = input().split()
print(solve(L, R))