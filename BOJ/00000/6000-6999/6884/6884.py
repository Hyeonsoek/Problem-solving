import sys
input = sys.stdin.readline
            
def is_prime(x):
    if x < 2:
        return False
    
    if x == 2:
        return True
    
    if not (x & 1):
        return False

    for xx in range(3, int(x ** .5) + 2):
        if x % xx == 0:
            return False
    
    return True

def solve():
    n, *arr = map(int, input().split())
    
    prefix = [0]
    for x in range(n):
        prefix.append(prefix[-1] + arr[x])
    
    for length in range(2, n + 1):
        for y in range(length, n + 1):
            if is_prime(prefix[y] - prefix[y - length]):
                print(f'Shortest primed subsequence is length {length}:', *arr[y - length:y])
                return
    
    print("This sequence is anti-primed.")

for _ in range(int(input())):
    solve()