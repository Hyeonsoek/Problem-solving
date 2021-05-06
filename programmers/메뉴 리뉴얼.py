def permute(order, permute_order, now, start):
    if len(now) > 1 and (now not in permute_order):
        permute_order.append(now)
        
    for idx in range(start, len(order)):
        now += order[idx]
        permute(order, permute_order, now, idx+1)
        now = now[:-1]
        
def solution(orders, course):
    answer = []
    
    menu = {}
    for order in orders:
        permute_order = []
        now = ""
        start = 0
        permute(order, permute_order, now, start)
        for per in permute_order:
            per = ''.join(sorted(list(per)))
            if per in menu:
                menu[per] += 1
            else :
                menu[per] = 1
    
    menu = { x : y for x, y in menu.items() if y > 1 }
    
    for cnt in course:
        temp = [ (x,y) for x,y in menu.items() if len(x) == cnt ]
        
        for x, y in temp:
            if y == max(list(zip(*temp))[1]):
                answer.append(x)
                
    answer.sort()
    
    return answer