def solve(string):
    target, guess = string.split()
    n = len(target)
    
    mtarget = [False] * n
    mguess = [False] * n
    
    black = 0
    for x in range(n):
        if target[x] == guess[x]:
            black += 1
            mtarget[x] = True
            mguess[x] = True
            
    grey = 0
    for x in range(n):
        if mtarget[x]:
            continue
        
        if x > 0 and target[x] == guess[x-1] and not mguess[x-1]:
            mtarget[x] = True
            mguess[x-1] = True
            grey += 1
        elif x < n - 1 and target[x] == guess[x+1] and not mguess[x+1]:
            mtarget[x] = True
            mguess[x+1] = True
            grey += 1
    
    white = 0
    for x in range(n):
        for y in range(n):
            if target[x] == guess[y] and not mtarget[x] and not mguess[y]:
                white += 1
                mtarget[x] = True
                mguess[x] = True
                break
    
    print(f'{guess}: {black} black, {grey} grey, {white} white')
    
while (test := input()) != '#':
    solve(test)