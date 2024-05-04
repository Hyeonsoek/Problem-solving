## ~ing

def is_dot(s1, s2):
    x1, y1, p1, q1 = s1
    x2, y2, p2, q2 = s2



    return False

for _ in range(4):
    array = list(int, input().split())
    x1, y1, p1, q1 = array[:4]
    x2, y2, p2, q2 = array[4:]

    if (x1 == x2 + p2) or (x2 == x1 + p1) \
            or (y1 == y2 + q2) or (y2 == y1 + q1):
        print('b')
    if is_dot(array[:4], array[4:]):
        print('c')
