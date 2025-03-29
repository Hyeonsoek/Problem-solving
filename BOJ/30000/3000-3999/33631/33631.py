def solve():
    f, c, e, b = map(int, input().split())
    fn, cn, en, bn = map(int, input().split())
    
    cookie = 0
    q = int(input())
    for _ in range(q):
        j, i = map(int, input().split())
        
        match j:
            case 1:
                n = min(f // fn, c // cn, e // en, b // bn)
                if n < i:
                    print('Hello, siumii')
                else:
                    f -= fn * i
                    c -= cn * i
                    e -= en * i
                    b -= bn * i
                    cookie += i
                    print(cookie)
            case 2:
                f += i
                print(f)
            case 3:
                c += i
                print(c)
            case 4:
                e += i
                print(e)
            case 5:
                b += i
                print(b)

solve()