answer = {'0123', '0145', '0246', '4567', '1357', '2367'}

n = int(input())
for x in range(n):
    print('YES' if ''.join(sorted(input().split())) in answer else 'NO')