def extend(borders, x):
    return [borders[0] - x, borders[1] + x, borders[2] - x, borders[3] + x]


def intersect(borders_a, borders_b):
    borders = [max(borders_a[0], borders_b[0]), min(borders_a[1], borders_b[1]),
               max(borders_a[2], borders_b[2]), min(borders_a[3], borders_b[3])]
    return borders


t, d, n = [int(x) for x in input().split()]
our_borders = [0, 0, 0, 0]
# min(y-x), max(y-x), min(y+x), max(y+x)
for _ in range(n):
    our_borders = extend(our_borders, t)
    x, y = [int(x) for x in input().split()]
    navigator_borders = [y - x - d, y - x + d, y + x - d, y + x + d]
    our_borders = intersect(our_borders, navigator_borders)

points = []
for diff_yx in range(our_borders[0], our_borders[1] + 1):
    for sum_yx in range(our_borders[2], our_borders[3] + 1):
        twice_y = diff_yx + sum_yx
        if twice_y % 2 == 0:
            y = twice_y//2
            x = y - diff_yx
            points.append([x, y])
print(len(points))
for point in points:
    print(*point)