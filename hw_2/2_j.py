n = int(input())
f_prev = float(input())
f_min = 30
f_max = 4000
for _ in range(n - 1):
    info = input().split()
    f, dist = float(info[0]), info[1]
    if (f > f_prev and dist == 'further') or (f < f_prev and dist == 'closer'):
        f_max = min(f_max, (f + f_prev)/2)
    else:
        f_min = max(f_min, (f + f_prev)/2)
    f_prev = f
print(f_min, f_max)