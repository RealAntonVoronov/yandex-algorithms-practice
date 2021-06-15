#sqrt(ax + b) = c
a, b, c = [int(input()) for _ in range(3)]
if a == 0:
	if b < 0:
		print('NO SOLUTION')
	elif b == c * c:
		print('MANY SOLUTIONS')
	else:
		print('NO SOLUTION')
elif c == 0:
	if b == 0:
		x = 0
	else:
		x = -b/a
	if int(x) * a + b == c * c:
		print(int(x))
	else:
		print('NO SOLUTION')
elif c < 0:
	print('NO SOLUTION')
else:
	x = (c * c - b)/a
	if int(x) * a + b == c * c:
		print(int(x))
	else:
		print('NO SOLUTION')
