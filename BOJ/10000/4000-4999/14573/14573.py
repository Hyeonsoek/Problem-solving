import sys
MAX = 10 ** 6 + 1
MOD = 10 ** 9 + 7
input = sys.stdin.readline
output = lambda x : sys.stdout.write(f'{x}\n')

def solve():
    po2 = 2
    cache = [0, 1, 1]
    prefix = [0, 1, 2]
    for _ in range(3, MAX):
        cache.append(prefix[-1] * po2)
        prefix.append((prefix[-1] + cache[-1]) % MOD)
        po2 = (po2 * 2) % MOD

    Q = int(input())
    
    for _ in range(Q):
        q, *arr = map(int, input().split())
        if 1 <= q <= 3:
            a, i, j = arr
            i, j = min(i, j), max(i, j)
            
            if q == 1:
                output((cache[i] * a) % MOD)
            elif q == 2:
                count = 0
                while not a & 1:
                    a >>= 1
                    count += 1
                if j <= 2:
                    output(count)
                else:
                    output(count + j - 1)
            else:
                output(((prefix[j] - prefix[i-1]) % MOD) * a % MOD)
        else:
            a, k = arr
            output((cache[k] * a) % MOD)

solve()