n = int(input())
x_coords = set()
for _ in range(n):
    bird_coords = [int(x) for x in input().split()]
    x_coords.add(bird_coords[0])

print(len(x_coords))
