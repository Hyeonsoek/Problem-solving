def solve():
    X, Y = map(int, input().split())
    
    cache = {x : 2 ** x - 1 for x in range(1, 65)}
    decompose = {x : [x-1, x-1, 1] for x in range(2, 65)}
    
    xx, yy = X, Y
    counterX = []
    counterY = []
    for key, value in sorted(cache.items(), reverse=True):
        while xx >= value:
            xx -= value
            counterX.append(key)
        
        while yy >= value:
            yy -= value
            counterY.append(key)
    
    counterX.sort()
    counterY.sort()
    
    if counterY:
        while len(counterX) - len(counterY) > 1 and counterY[-1] > 1:
            counterY.extend(decompose[counterY.pop()])
            counterY.sort()
    
    if counterX:
        while len(counterY) - len(counterX) > 1 and counterX[-1] > 1:
            counterX.extend(decompose[counterX.pop()])
            counterX.sort()
    
    if abs(len(counterX) - len(counterY)) > 1:
        print('impossible')
        return
    
    result = ''
    if len(counterX) - len(counterY) in [0, 1]:
        while counterX or counterY:
            if counterX:
                result += counterX.pop() * 'R'
            
            if counterY:
                result += counterY.pop() * 'U'
    else:
        while counterX or counterY:
            if counterY:
                result += counterY.pop() * 'U'
            
            if counterX:
                result += counterX.pop() * 'R'
    
    print(result if len(result) <= 4000 else 'impossible')

solve()