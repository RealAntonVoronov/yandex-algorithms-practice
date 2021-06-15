lengths = [int(input()) for _ in range(3)]
answer = 'YES'

for i in range(3):
	checker = (lengths[i % 3] + lengths[(i + 1) % 3] > lengths[(i + 2) % 3])
	if not checker:
		answer = 'NO'

print(answer)
