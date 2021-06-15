a, b, c, d, e = [int(input()) for _ in range(5)]
a, b, c = sorted([a, b, c])
d, e = sorted([d, e])
if a <= d and b <= e:
    print('YES')
else:
    print('NO')
