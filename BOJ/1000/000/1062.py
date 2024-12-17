from itertools import combinations

default_set = set("antatica")

n, k = map(int, input().split())

list_string = []

for _ in range(n):
    string = input()[4:-4]
    
    value = 0
    for x in set(string) - default_set:
        value |= (1 << (ord(x) - ord('a')))
        
    list_string.append(value)

if len(default_set) > k:
    print(0)
else:
    max_value = 0

    list_chr = [ 2 ** x for x in range(26) ]
    
    for x in default_set:
        list_chr.remove(2 ** (ord(x) - ord('a')))

    for comb in combinations(list_chr, k - 5):
        count = 0
        value = sum(comb)
        
        for string in list_string:
            if string & value == string:
                count += 1
        
        max_value = max(max_value, count)

    print(max_value)