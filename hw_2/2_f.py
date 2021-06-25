n = int(input())
a = [int(x) for x in input().split()]
b = a[::-1]
if a == b:
    n_min = 0
else:
    for i in range(len(a)):
        res = a + b[i:]
        if res == res[::-1]:
            n_min = len(a) - i
            i_best = i
print(n_min)
if n_min > 0:
    print(*b[i_best:])
