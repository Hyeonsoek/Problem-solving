n, k = map(int, input().split())
string = list(input())
a = ord('A')

for x in range(n):
    value = ord(string[x]) - a
    if value > 0 and 26 - value <= k:
        string[x] = 'A'
        k -= 26 - value

string[-1] = chr((ord(string[-1]) - a + k) % 26 + a)
print(''.join(string))