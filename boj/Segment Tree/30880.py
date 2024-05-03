import sys, math
input = sys.stdin.readline
MOD = 1000000007
R, RO, ROC, ROCK = 0, 1, 2, 3
O, C, K, OC, CK, OCK = 0, 1, 2, 3, 4, 5

def rock_index(value):
    if value == "R":
        return R
    return -1

def ock_index(value):
    match value:
        case "O":
            return O
        case "C":
            return C
        case "K":
            return K
    return -1

def make_new(value):
    _rock = [0] * 4
    _ock = [0] * 6
    
    index_rock = rock_index(value)
    if index_rock > -1:
        _rock[index_rock] += 1
    
    index_ock = ock_index(value)
    if index_ock > -1:
        _ock[index_ock] += 1
    
    return (1, _rock, _ock)

def fastExp(a, x):
    result = 1
    while x > 0:
        if x & 1:
            result = (a * result) % MOD
        a = (a * a) % MOD
        x >>= 1
    return result

def mix(left, right):
    left_len, lr, lo = left
    right_len, rr, ro = right

    _rock, _ock = [0] * 4, [0] * 6
    
    _ock[O] = (lo[O] + ro[O]) % MOD
    _ock[C] = (lo[C] + ro[C]) % MOD
    _ock[K] = (lo[K] + ro[K]) % MOD
    
    _ock[OC] = ((lo[O] * ro[C]) + lo[OC] + ro[OC]) % MOD
    _ock[CK] = ((lo[C] * ro[K]) + lo[CK] + ro[CK]) % MOD
    
    _ock[OCK] = ((lo[OC] * ro[K]) + (lo[O] * ro[CK])\
                    + lo[OCK] + ro[OCK]) % MOD

    value = fastExp(2, left_len)
    _rock[R] = (lr[R] + (value * rr[R])) % MOD
    _rock[RO] = (lr[RO] + (lr[R] * ro[O]) + (value * rr[RO])) % MOD
    
    _rock[ROC] = (lr[ROC] + (value * rr[ROC]) + (lr[RO] * ro[C]) + (lr[R] * ro[OC])) % MOD
    _rock[ROCK] = (lr[ROCK] + (value * rr[ROCK]) + (lr[ROC] * ro[K]) + (lr[RO] * ro[CK]) + (lr[R] * ro[OCK])) % MOD
    
    return (left_len + right_len, _rock, _ock)

def init(node, start, end):
    if start == end:
        new = make_new(array[start])
        tree[node] = new
        return tree[node]
    
    mid = (start + end) // 2
    LL = init(node * 2, start, mid)
    RR = init(node * 2 + 1, mid + 1, end)
    
    tree[node] = mix(LL, RR)
    return tree[node]

def update(node, start, end, index, value):
    if index < start or end < index:
        return tree[node]
    
    if start == end:
        new = make_new(value)
        tree[node] = new
        return tree[node]
    
    mid = (start + end) // 2
    LL = update(node * 2, start, mid, index, value)
    RR = update(node * 2 + 1, mid + 1, end, index, value)
    
    tree[node] = mix(LL, RR)
    return tree[node]

def query(node, start, end, left, right):
    if right < start or end < left:
        return (0, [0] * 4, [0] * 6)
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = query(node * 2, start, mid, left, right)
    RR = query(node * 2 + 1, mid + 1, end, left, right)
    
    return mix(LL, RR)

n = int(input())
array = [""] + list(input())

# L | ROCK - (ROC - K) - (RO - CK) - (R - OCK) - ROCK | R

width = 1 << (math.ceil(math.log2(n)) + 1) + 1
tree = [ (0, [0] * 4, [0] * 6) for _ in range(width) ]

init(1, 1, n)

m = int(input())
for _ in range(m):
    a, b, c = input().split()
    
    if a == '2':
        b, c = int(b), int(c)
        _, _rock, _ = query(1, 1, n, b, c)
        print(_rock[3])
    else:
        update(1, 1, n, int(b), c)

# 시간 줄이는 방법
# 1. 리스트 부분 단순 튜플로 바꾸기 (알아보긴 힘들지만 좋다)
# 2. 2의 거듭제곱 미리 구하기(상수니깐 미리 구해놔도 된다!!)