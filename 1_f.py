a, b, c, d = [int(x) for x in input().split()]
min_s = 1e7
res = []

s = (a + c) * max(b, d)
if s < min_s:
    min_s = s
    res = [a + c, max(b, d)]

s = (a + d) * max(b, c)
if s < min_s:
    min_s = s
    res = [a + d, max(b, c)]

s = (b + c) * max(a, d)
if s < min_s:
    min_s = s
    res = [b + c, max(a, d)]

s = (b + d) * max(a, c)
if s < min_s:
    min_s = s
    res = [b + d, max(a, c)]
print(*res)
