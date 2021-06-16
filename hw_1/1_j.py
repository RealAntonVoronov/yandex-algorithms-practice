def my_solve(a, b, c, d, e, f):
    if a == 0:
        if b == 0:
            if c == 0:
                if d == 0:
                    if e == 0:
                        if f == 0:
                            print(5)
                        else:
                            print(0)
                    else:
                        print(0)
                elif e == 0:
                    y = f / d
                    print(4, f'{y:.5f}')
                else:
                    print(0)
            elif d == 0:
                if e == 0:
                    x = f / c
                    print(3, f'{x:.5f}')
                else:
                    print(0)
            elif e == 0:
                k = -c / d
                m = f / d
                print(1, f'{k:.5f} {m:.5f}')
            else:
                print(0)
        elif c == 0:
            if d == 0:
                if f == 0:
                    y = e / b
                    print(4, f'{y:.5f}')
                else:
                    print(4, 0)
            else:
                if e / b == f / d:
                    y = e / b
                    print(4, f'{y:.5f}')
                else:
                    print(0)
        else:
            y = e / b
            x = (f - d * y) / c
            print(2, f'{x:.5f} {y:.5f}')
    elif b == 0:
        x = e / a
        if d == 0:
            if c == 0:
                if f == 0:
                    print(3, f'{x:.5f}')
                else:
                    print(0)
            elif e / a == f / c:
                print(3, f'{x:.5f}')
            else:
                print(0)
        else:
            y = (f - c * x) / d
            print(2, f'{x:.5f} {y:.5f}')
    elif c == 0:
        if d == 0:
            if f == 0:
                k = -a / b
                m = e / b
                print(1, f'{k:.5f} {m:.5f}')
            else:
                print(0)
        else:
            y = f / d
            x = (e - b * y) / a
            print(2, f'{x:.5f} {y:.5f}')
    elif d == 0:
        x = f / c
        y = (e - a * x) / b
        print(2, f'{x:.5f} {y:.5f}')
    elif a * d == b * c:
        if f * a == c * e:
            k = -a / b
            m = e / b
            print(1, f'{k:.5f} {m:.5f}')
        else:
            print(0)
    else:
        y = (f * a - c * e) / (a * d - b * c)
        x = (e - b * y) / a
        print(2, f'{x:.5f} {y:.5f}')


a, b, c, d, e, f = [float(input()) for _ in range(6)]
my_solve(a, b, c, d, e, f)
