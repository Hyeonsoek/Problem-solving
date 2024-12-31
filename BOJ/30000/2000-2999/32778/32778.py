def solve():
    string = input().replace('(', '*').replace(')', '').split('*')
    
    print(string[0])
    if len(string) == 2:
        print(string[1])
    else:
        print('-')

solve()