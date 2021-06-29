n = int(input())
durability = [0]
durability.extend([int(x) for x in input().split()])  # len = n + 1
total = int(input())
sequence = [int(x) for x in input().split()]  # len = total
for i in range(total):
    durability[sequence[i]] -= 1
for i in range(1, n + 1):
    if durability[i] >= 0:
        print('NO')
    else:
        print('YES')