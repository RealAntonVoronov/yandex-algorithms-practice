#a = [int(x) for x in input().split()]
with open('../../../Downloads/Telegram Desktop/004') as f:
    a = [int(x) for x in f.readlines()[0].strip().split()]
    print(a)
if len(a) < 2:
    print('NO')
else:
    flag = True
    for i in range(1, len(a)):
        if a[i] <= a[i-1]:
            flag = False
            print('NO')
            break
    if flag:
        print('YES')