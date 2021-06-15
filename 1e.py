import math

k_1, m, k_2, p_2, n_2 = [int(x) for x in input().split()]

if n_2 > m or k_2 < (p_2 - 1) * m + n_2:
    p_1, n_1 = -1, -1
elif p_2 == 1 and n_2 == 1:
    if k_1 > k_2:
        p_1 = 0
        if m > 1:
            n_1 = 0
            if k_1 < m * n_2:
                p_1 = 1
        else:
            n_1 = 1
    else:
        p_1, n_1 = 1, 1
else:
    p_variants, n_variants = [], set()

    full_levels = m * (p_2 - 1) + n_2 - 1
    flats_per_level_max = (k_2 - 1) // full_levels
    flats_per_level_min = math.ceil(k_2 / (full_levels + 1))
    x_variants = [i for i in range(flats_per_level_min, flats_per_level_max + 1)]

    if flats_per_level_min > flats_per_level_max:
        p_1, n_1 = -1, -1
    else:
        for i in range(len(x_variants)):
            x = x_variants[i]
            if k_1 % (x * m) == 0:
                p_variants.append(k_1 // (x * m))
            else:
                p_variants.append(k_1 // (x * m) + 1)
        for i in range(len(x_variants)):
            x = x_variants[i]
            p_1 = p_variants[i]
            flats_before = (p_1 - 1) * m * x
            if (k_1 - flats_before) % x == 0:
                n_variants.add((k_1 - flats_before) // x)
            else:
                n_variants.add((k_1 - flats_before) // x + 1)
        if len(set(p_variants)) > 1:
            p_1 = 0
        else:
            p_1 = p_variants[0]
        if len(n_variants) > 1:
            n_1 = 0
        else:
            n_1 = n_variants.pop()
print(p_1, n_1)
