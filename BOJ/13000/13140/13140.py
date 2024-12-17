# s = set('helloworld')
# slist = list(s)

# def solve(k, valuedict, numbers):
#     if k == 7:
#         hello = int(''.join(map(lambda x : valuedict[x], 'hello')))
#         world = int(''.join(map(lambda x : valuedict[x], 'world')))

#         if hello + world == answer:
#             print(f'{hello:7d}')
#             print(f'+{world:6d}')
#             print('-------')
#             print(f'{answer:7d}')
#             return True
#         return False

#     newnumbers = set(numbers)
#     for x in numbers:
#         if x == 0 and slist[k] in {'w', 'h'}:
#             continue
        
#         newnumbers.remove(x)
#         valuedict[slist[k]] = f'{x}'
        
#         if solve(k + 1, valuedict, newnumbers):
#             return True
        
#         newnumbers.add(x)
#         valuedict[slist[k]] = '-1'
    
#     return False
    
    
# answer = int(input())
# if not solve(0, {x : '-1' for x in s}, set(range(10))):
#     print('No Answer')

from itertools import combinations, permutations

def solve():
    n = int(input())
    s = set('helloworld')

    numbers = map(str, range(10))
    for comb in combinations(numbers, 7):
        for perm in permutations(s):
            valuedict = {char : value for value, char in zip(comb, perm)}
            if valuedict['h'] == '0' or valuedict['w'] == '0':
                continue
            
            hello = int(''.join(map(lambda x : valuedict[x], 'hello')))
            world = int(''.join(map(lambda x : valuedict[x], 'world')))

            if hello + world == n:
                print(f'{hello:7d}')
                print(f'+{world:6d}')
                print('-------')
                print(f'{n:7d}')
                return True
    
    return False

if not solve():
    print('No Answer')