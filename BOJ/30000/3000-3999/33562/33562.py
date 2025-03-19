import sys
from collections import deque
input = sys.stdin.readline

def toFloor(iterable):
    return ''.join(iterable)

def toShape(iterable):
    values = []
    for i in iterable:
        if i != '--------':
            values.append(i)
    return ':'.join(values)

def floor_to_list(floor : str):
    return [floor[i:i+2] for i in range(0, 8, 2)]

def cut_floor(floor : str):
    return '----' + floor[4:], floor[:4] + '----'

def cut_shape(shape : str):
    if shape:
        left, right = zip(*[cut_floor(i) for i in shape.split(':')])
        return toShape(left), toShape(right)
    return '', ''

def rotate_floor(floor : str, count):
    queue = deque(floor_to_list(floor))
    queue.rotate(count)
    return toFloor(queue)

def rotate_shape(shape : str, count):
    if shape:
        return toShape([rotate_floor(i, count) for i in shape.split(':')])
    return shape

def paint_floor(floor : str, color : str):
    ret = list(floor)
    for i in range(0, 8, 2):
        if floor[i] != '-':
            ret[i+1] = color
    return ''.join(ret)

def paint_shape(shape : str, color : str):
    if shape:
        return toShape([paint_floor(i, color) for i in shape.split(':')])
    return shape

def is_combinable(floor1 : str, floor2 : str):
    xx = floor_to_list(floor1)
    yy = floor_to_list(floor2)
    for i in range(4):
        if xx[i] != '--' and yy[i] != '--':
            return False
    return True

def find_combinable_depth(n : int, floors1 : list[str], m : int, floors2 : list[str]):
    s = n - 1
    k = min(n, m)
    before, length = 0, 1
    while s >= 0:
        for i in range(s, s + length):
            if not is_combinable(floors1[i], floors2[i - s]):
                return s + 1, before
    
        s -= 1
        before = length
        if length < k:
            length += 1
    
    return 0, length
    
def combine_floor(floor1 : str, floor2 : str):
    zz = []
    xx = floor_to_list(floor1)
    yy = floor_to_list(floor2)
    for i in range(4):
        if xx[i] == '--':
            zz.append(yy[i])
        else:
            zz.append(xx[i])
    
    return toFloor(zz)

def combine_shape(shape1 : str, shape2 : str):
    if shape1 == '' or shape2 == '':
        return ''
    
    floors1 = shape1.split(':')
    floors2 = shape2.split(':')
    floors3 = []
    
    n = len(floors1)
    m = len(floors2)
    
    s, d = find_combinable_depth(n, floors1, m, floors2)
    
    for i in range(s):
        floors3.append(floors1[i])
        
    for i in range(s, s + d):
        floors3.append(combine_floor(floors1[i], floors2[i - s]))
    
    if d < m:
        for i in range(d, m):
            floors3.append(floors2[i])
    else:
        for i in range(s + d, n):
            floors3.append(floors1[i])
    
    floors3 = floors3[:4]
    return toShape(floors3)

def solve():
    n, m = map(int, input().split())
    shapes = [ input().strip() for _ in range(n) ]
    for _ in range(n, 100):
        shapes.append('')

    for _ in range(m):
        q, i, j, k = input().split()
        i = int(i) - 1
        j = int(j) - 1
        
        match q:
            case '1':
                k = int(k) - 1
                shapes[j], shapes[k] = cut_shape(shapes[i])
            case '2':
                k = int(k)
                shapes[j] = rotate_shape(str(shapes[i]), k)
            case '3':
                k = int(k) - 1
                shapes[k] = combine_shape(shapes[i], shapes[j])
            case '4':
                shapes[j] = paint_shape(str(shapes[i]), k)
        
    if shapes[99] == '':
        print("None")
    else:
        print(shapes[99])

solve()

# print(cut_shape('CrRwWu--') == ('----Wu--', 'CrRw----'))
# print(cut_shape('CuCu----:--RuRu--:Wu------') == ('----Ru--', 'CuCu----:--Ru----:Wu------'))
# print(cut_shape('--Rc----:Sw------') == ('', '--Rc----:Sw------'))

# print(paint_shape('CrRwWu--', 'c') == 'CcRcWc--')
# print(paint_shape('CuCw----:--RyRg--:Wb------', 'b') == 'CbCb----:--RbRb--:Wb------')

# print(rotate_shape('CrRwWu--', 1) == '--CrRwWu')
# print(rotate_shape('CuCu----:--RuRu--:Wu------', 2) == '----CuCu:Ru----Ru:----Wu--')
# print(rotate_shape('CuCu----:--RuRu--:Wu------', 3) == 'Cu----Cu:RuRu----:------Wu')

# print(combine_shape("CuCu----", "----RuRu") == "CuCuRuRu")
# print(combine_shape("CuCu----", "--RuRu--") == "CuCu----:--RuRu--")
# print(combine_shape("Ru----Ru:Ru----Ru:RuRuRuRu", "--CuCu--:--CuCu--") == "Ru----Ru:Ru----Ru:RuRuRuRu:--CuCu--")
# print(combine_shape("RuRuRuRu:RuRuRuRu:RuRu----:RuRu----", "----CuCu:CuCuCuCu:CuCuCuCu") == "RuRuRuRu:RuRuRuRu:RuRu----:RuRuCuCu")