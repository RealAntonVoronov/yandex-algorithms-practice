n = int(input())
blocks = {}
res = 0
for i in range(n):
    width, height = [int(x) for x in input().split()]
    blocks.setdefault(width, []).append(height)

for width in sorted(blocks.keys(), reverse=True):
    res += max(blocks[width])

print(res)
