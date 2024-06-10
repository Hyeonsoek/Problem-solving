def solve():
    '''
    edge = 2w + 2h - 8
    centre = (w - 2) * (h - 2) = wh - (2w + 2h - 4)
    
    wh = centre + edge + corner
    w + h = (edge + 4) // 2
    w - h = ((w + h) ** 2 - 4wh) ** .5
    
    2w = w + h + ((w + h) ** 2 - 4wh) ** .5
    '''
    corner, edge, centre = map(int, input().split())

    if corner != 4 or edge % 2:
        return 'impossible'
    
    wph = edge // 2 + corner
    wh = corner + edge + centre
    
    if wph ** 2 < 4 * wh:
        return 'impossible'
    
    wmh = (wph ** 2 - 4 * wh) ** .5
    
    if not wmh.is_integer():
        return 'impossible'
    
    w = int(wph + wmh) // 2
    h = wh // w
    
    if w * h != wh:
        return 'impossible'
    
    return f'{w} {h}'
    
print(solve())