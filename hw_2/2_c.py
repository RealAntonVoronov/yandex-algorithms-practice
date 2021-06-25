n = int(input())
if n == 0:
    print(None)
else:
    a = [int(x) for x in input().split()]
    x = int(input())

    ans = 0
    min_res = abs(a[0] - x)
    for i in range(1, n):
        res = abs(a[i] - x)
        if res < min_res:
            min_res = res
            ans = i
    print(a[ans])
