a = [int(input())]
while True:
    x = int(input())
    if x == -2 * (10 ** 9):
        break
    a.append(x)
if len(a) < 2:
    print('RANDOM')
options = {'CONSTANT' : False, 'ASCENDING' : True, 'WEAKLY ASCENDING' : True,
           'DESCENDING' : True, 'WEAKLY DESCENDING' : True, 'RANDOM' : False}
if len(set(a)) == 1:
    options['CONSTANT'] = True
elif len(set(a)) == len(a):
    options['WEAKLY ASCENDING'] = False
    options['WEAKLY DESCENDING'] = False
else:
    options['ASCENDING'] = False
    options['DESCENDING'] = False

for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        options['DESCENDING'] = False
        options['WEAKLY DESCENDING'] = False
    elif a[i] < a[i - 1]:
        options['ASCENDING'] = False
        options['WEAKLY ASCENDING'] = False
    elif a[i] == a[i - 1]:
        options['ASCENDING'] = False
        options['DESCENDING'] = False

if options['CONSTANT']:
    print('CONSTANT')
else:
    res = 0
    for key, value in options.items():
        res += int(value)
    if res == 1:
        for key, value in options.items():
            if value:
                print(key)
    else:
        print('RANDOM')