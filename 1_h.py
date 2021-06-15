a, b, n, m = [int(input()) for _ in range(4)]

# to see at least n trains she should stay for at least:
ta_min = n * (a + 1) - a
ta_max = n * (a + 1) + a

tb_min = m * (b + 1) - b
tb_max = m * (b + 1) + b

if tb_min > ta_max or tb_max < ta_min:
    print(-1)
else:
    print(max(ta_min, tb_min), min(ta_max, tb_max))
