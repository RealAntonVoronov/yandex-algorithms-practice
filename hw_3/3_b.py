a_1 = set([int(x) for x in input().split()])
a_2 = set([int(x) for x in input().split()])
print(*sorted(a_1.intersection(a_2)))