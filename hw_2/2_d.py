a = [float(x) for x in input().split()]
res = 0
if len(a) >= 3:
    for i in range(1, len(a) - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            res += 1
print(res)